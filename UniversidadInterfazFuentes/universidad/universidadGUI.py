import os.path
import PySimpleGUIQt as sg
from minizinc import Instance, Model, Solver


wTitle = 'Ubicación Universidad'
location = (None, None)
tMunicipio = '        Municipios        '
n = ''
m = 0
dataName = 'Datos.dzn'


def resolver(model, file):
    modelo = Model(model)
    gecode = Solver.lookup("gecode")
    modelo.add_file(file)
    instance = Instance(gecode, modelo)
    result = instance.solve()
    rtn = result["posUniversidad"]
    rtn.append(round(pow(result["largestDistance"], 0.5), 2))
    return rtn


def makeLayout():
    global n
    global m
    data_column = [
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
    result_column = [
        [
            sg.Stretch(),
            sg.Text('RESULTADO'),
            sg.Stretch()
        ],
        [
            sg.Multiline(size=(40, m+5), key='textbox')
        ]
    ]
    layout = [
        [
            sg.Column(data_column),
            sg.VSeperator(),
            sg.Column(result_column),
        ]
    ]
    return layout


def Main(model):
    # test()
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
                    aux = resolver(model, dataName)
                    result = \
                        "     Ubicación de la Universidad:\n" + \
                        "Este:\t" + str(aux[0]) + " Km\n" + \
                        "Norte:\t" + str(aux[1]) + " Km\n" + \
                        "\n  Distancia más larga:  " + str(aux[2]) + " Km"

                    window['textbox'].update(result)
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
        archivo = open(dataName, "w")
        archivo.write(newData)
        archivo.close()

    except:
        err()


def err():
    print("something's wrong")


def test():
    print(
        resolver("../Universidad.mzn", '../MisInstancias/Datos.dzn'))
    exit()
