import PySimpleGUIQt as sg
import os.path

# sg.theme('Reddit')   # Add a touch of color

layout = [
    [
        sg.Stretch(),
        sg.Text('Bienvenido a ...'),
        sg.Stretch()
    ],
    [
        sg.Text('Tamaño del cuadrado (n)'),
        sg.Stretch(),
        sg.InputText(enable_events=True, key="-N-")
    ],
    [
        sg.Text('Número de municipios (m)'),
        sg.Stretch(),
        sg.InputText(enable_events=True, key="-M-")
    ],
    [],
    [
        sg.Button('Ok'),
        sg.Button('Cancel')
    ]
]


def Main():
    #  testWin()
    window = sg.Window('Universidad', layout)
    while True:
        e, values = window.read()
        if e == sg.WIN_CLOSED or e == 'Cancel':
            break
        elif e == '-N-':
            updateN(values['-N-'])
        elif e == "-M-":
            updateM(values['-M-'])
        print(values)
    window.close()


def updateN(N):
    print(N)


def updateM(M):
    print(M)


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
