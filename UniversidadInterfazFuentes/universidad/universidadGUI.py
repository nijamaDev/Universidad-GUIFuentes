import os.path
import PySimpleGUIQt as sg
from minizinc import Instance, Model, Solver


wTitle = 'Ubicación Universidad'
location = (None, None)
tMunicipio = '        Municipios        '
n = ''
m = 0


def resolver(n, m, ciudades, mod):
    modelo = Model(mod)
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, modelo)
    instance["n"] = n
    instance["m"] = m
    instance["ciudades"] = ciudades
    result = instance.solve()
    rtn = result["posUniversidad"]
    rtn.append(round(pow(result["largestDistance"], 0.5), 2))
    return rtn


# sg.theme('DarkBrown4')   # Add a touch of color


def makeLayout():
    global n
    global m
    layout = [
        [
            sg.Stretch(),
            sg.Text('Por favor, ingrese los siguientes datos:'),
            sg.Stretch()
        ],
        [
            sg.Text('Tamaño del cuadrado (n)'),
            sg.Stretch(),
            sg.InputText(
                default_text=n,
                key="-N-",
                justification="center",
                background_color="#dee",
                size=(4, 0.7))
        ],
        [
            sg.Text('Número de municipios (m)'),
            sg.Stretch(),
            sg.InputText(
                default_text=m,
                key="-M-",
                justification="center",
                background_color="#dee",
                size=(4, 0.7))
        ],
        [],
        [
            sg.Stretch(),
            sg.Button(tMunicipio),
            sg.Stretch()
        ],
        *[
            [
                sg.Stretch(),
                sg.Text("Ciudad "+str(i+1)+":"),
                sg.InputText(
                    default_text='0,0',
                    key="ciudad"+str(i),
                    justification="center",
                    background_color="#dee",
                    size=(6, 0.7)
                ),
                sg.Stretch()]
            for i in range(m)
        ],
        [sg.Button('Generar archivo',  key='-DATA-')]
    ]
    return layout


def Main(model):
    # testWin()
    # test(model)
    global n
    global m
    window = sg.Window(wTitle, makeLayout(), location=location)
    while True:
        ev, values = window.read()
        if ev == sg.WIN_CLOSED or ev == 'Cancel':
            break
        elif ev == tMunicipio:
            try:
                m = int(values['-M-'])
                n = int(values['-N-'])
            except:
                err()
            windowNew = sg.Window(wTitle, makeLayout(), location=location)
            window.Close()
            window = windowNew
        elif ev == '-DATA-':
            try:
                if (n > 0 and m > 0):
                    makeData(values)
                    evalueData(values)
            except:
                err()
    window.close()


def makeData(values):
    global n
    global m
    try:
        newData = \
            "n=" + str(n) + ";\n" + \
            "m=" + str(m) + ";\n" + \
            "ciudades=[|" + \
            "\n|".join([values['ciudad'+str(i)] for i in range(m)]) \
            + "|];"
        archivo = open("Datos.dzn", "w")
        archivo.write(newData)
        archivo.close()

    except:
        err()


def err():
    print('no mi rey')


def test(model):
    print(
        resolver(
            10, 10,
            [
                [0, 1],
                [2, 4],
                [3, 8],
                [4, 1],
                [6, 3],
                [6, 4],
                [6, 5],
                [8, 7],
                [9, 3],
                [9, 10]
            ], model))
    exit()


def testWin():
    # First the window layout in 2 columns
    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    # ----- Full layout -----

    layout = [
        [
            sg.Column(file_list_column, key="-TEST-"),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                # window["-TEST-"].update(sg.VSeperator())
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)
            except:
                pass

    window.close()
