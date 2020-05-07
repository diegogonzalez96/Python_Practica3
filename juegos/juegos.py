import hangman
import reversegam
import tictactoeModificado
from datetime import datetime
import json
import PySimpleGUI as sg
from os.path import isfile

# ------------------- FUNCIONES ---------------------		


def save_data(ruta, data):                                          #guardo los datos en JSON
    d = {}
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")        #Mostrar la fecha de cuando se guarda el archivo
    print("date and time =", dt_string)

    d[dt_string] = data
    if isfile(ruta):                                                #SI EL ARCHIVO EXISTE LO LEO, LO MODIFICO Y LUEGO LO ESCRIBO DE NUEVO
        with open(ruta, 'r') as arc:
            lista = json.load(arc)
            lista.append(d)
        with open (ruta, 'w') as arc2:          
            json.dump(lista, arc2)
    else:                                                           #SI NO EXISTE LO CREO Y ESCRIBO
        with open(ruta, 'w') as arc3:
            lista = [d]
            json.dump(lista, arc3)

def printJson(ruta):                                                #IMPRIMO EL ARCHIVO JSON
    with open(ruta, 'r') as arc:
        dato = json.load(arc)
    print(json.dumps(dato, indent=4))

def add(player, game, dicc):                                         #AGREGO LOS DATOS AL DICCIONARIO
    dicc[player] = game

def mainGames(ruta):						#------------------ MENU DEL JUEGO -------------------------
    dicc = {}
    sigo_jugando = True
    while sigo_jugando:							    #PRIMER CORTE DE CONTROL PARA VER SI SIGO JUGANDO O NO
        sg.theme('Dark Teal 9')
        layout = [								    #DISEÑO DE LA PRIMER VENTANA
                [sg.Text('INGRESE NOMBRE DE JUGADOR', size=(50, 1), justification='center', font=("Courier", 18))],
                [sg.Input(key='player',justification='center', size=(90,3), font=('Courier', 10))],
                [sg.ReadButton('OK'), sg.ReadButton('CANCEL')]
                ]
        window = sg.Window('SELECCION DE NOMBRE', layout)
        event, values = window.Read()
        window.close()							    #UNA VEZ USADA CIERRO PRIMER VENTANA

        if event in (None, 'CANCEL'):
            break
        else:
            if event is 'OK':
                layout2 = [						    #DISEÑO DE LA SEGUNDA VENTANA
                        [sg.Text('SELECCIONE UN JUEGO ', size=(25,2), justification='center', font=('Courier', 20))],
                        [sg.ReadButton('AHORCADO', size=(50,2))],
                        [sg.ReadButton('TA-TE-TI', size=(50,2))],
                        [sg.ReadButton('OTELLO', size=(50,2))],
                        [sg.ReadButton('SALIR', size=(50,2))]
                        ]

                window = sg.Window('MENU', layout2)
                event2, values2 = window.Read()
                window.close()                      #UNA VEZ USADA CIERRO SEGUNDA VENTANA
                                                    #POSIBLES ELECCIONES
                if event2 == 'AHORCADO':
                    hangman.main()
                    game = 'AHORCADO'
                    add(values['player'], game, dicc)
                    save_data(ruta, dicc)
                elif event2 == 'TA-TE-TI':
                    tictactoeModificado.main()
                    game = 'TA-TE-TI'
                    add(values['player'], game, dicc)
                    save_data(ruta, dicc)
                elif event2 == 'OTELLO':
                    reversegam.main()
                    game = 'OTELLO'
                    add(values['player'], game, dicc)
                    save_data(ruta, dicc)
                elif event2 == 'SALIR':
                    save_data(ruta, dicc)
                    sigo_jugando = False		    #SI DECIDO SALIR CAMBIO LA CONDICION DEL PRIMER CORTE DE CONTROL
                    break

#---------- PROGRAMA PRINCIPAL ---------

ruta = 'jugadorJuego.json'
mainGames(ruta)
printJson(ruta)