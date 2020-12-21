import random
from tkinter import messagebox as mb

# Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
def validoIntento(intento, letrasTotales):
    mensaje = ''
    response = False
    intento = intento.lower()
    if (intento == ''):
        mensaje = 'Por favor, introduce una letra.'
        mb.showwarning(message=mensaje, title="!Atencion")
    elif intento in letrasTotales:
        mensaje = 'Ya has probado esa letra. Elige otra.'
        mb.showwarning(message=mensaje, title="!Atencion")
    elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
        mensaje = 'Por favor ingresa una LETRA.'
        mb.showwarning(message=mensaje, title="!Atencion")
    else:
        response = True
    return response

def jugada(intento,palabraSecreta,letrasCorrectas,letrasIncorrectas, arrayImagenes):
    msgResponse = ""
    response = ""
    if intento in palabraSecreta:
        response =  'letraCorrecta'
        palabraTotal = validoPalabraTotal(palabraSecreta,letrasCorrectas + intento)
        if(palabraSecreta == palabraTotal):
                msgResponse= '¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!\n ¿Desea jugar de Nuevo?"'
                seguirJugando = mb.askretrycancel(message=msgResponse, title="Felicitaciones :D")
                if(seguirJugando):
                    response = 'seguirJugando'
                else: response =  'juegoGanado'
    else:
            # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(arrayImagenes) - 1:
            msgDiaglog = '¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"'
            mb.showerror(message=msgDiaglog, title="Que Mal :'(")
            response = 'juegoPerdido'
        else: response = 'letraIncorrecta'
    return response

    

def letraOculta(palabraSecreta,letrasCorrectas):
    espaciosVacíos = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + \
            palabraSecreta[i] + espaciosVacíos[i+1:]
    palabra = ""
    for letra in espaciosVacíos:
        palabra = palabra +  letra + " "
    return palabra.upper()

def validoPalabraTotal(palabraSecreta,letrasCorrectas):
    espaciosVacíos = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + \
            palabraSecreta[i] + espaciosVacíos[i+1:]
    palabra = ""
    for letra in espaciosVacíos:
        palabra = palabra +  letra
    return palabra.lower()

