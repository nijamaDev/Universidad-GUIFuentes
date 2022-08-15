import os.path
import PySimpleGUIQt as sg
from minizinc import Instance, Model, Solver


wTitle = 'Universidad'
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


# sg.theme('Reddit')   # Add a touch of color
def makeLayout():
    global n
    global m
    layout = [
        [
            sg.Stretch(),
            sg.Text('Bienvenido a Universidad solver'),
            sg.Stretch()
        ],
        [
            sg.Text('Tamaño del cuadrado (n)'),
            sg.Stretch(),
            sg.InputText(
                default_text=n,
                enable_events=True,
                key="-N-",
                size=(4, 0.7))
        ],
        [
            sg.Text('Número de municipios (m)'),
            sg.Stretch(),
            sg.InputText(
                default_text=m,
                enable_events=True,
                key="-M-",
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
                    key="ciudad"+str(i+1),
                    size=(4, 0.7)
                ),
                sg.Stretch()]
            for i in range(m)
        ],
        [sg.Button('Salir')]
    ]
    return layout


def Main(model):
    # testWin()
    # test(model)
    location = (None, None)
    window = sg.Window(wTitle, makeLayout(), location=location)
    while True:
        ev, values = window.read()
        if ev == sg.WIN_CLOSED or ev == 'Cancel':
            break
        elif ev == tMunicipio:
            try:
                global n
                global m
                n = int(values['-N-'])
                m = int(values['-M-'])
            except:
                err()
            print(n)
            windowNew = sg.Window(wTitle, makeLayout(), location=location)
            window.Close()
            window = windowNew
    window.close()


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
