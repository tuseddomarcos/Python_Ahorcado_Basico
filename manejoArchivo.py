import csv
import random
from tkinter import messagebox as mb

#Leo el archivo .csv y busco por nivel, luego busco una palabra ramdon y la retorno.
def seleccionoPalabrasPorNivel(nivel):
    listPalabras = []
    reader = csv.reader(open('ListaPalabras/ListaPalabras.csv'))
    for row in reader:
        listPalabras.append(row)
    #Obtengo palabra al azar
    palabra = obtenerPalabraAlAzar(listPalabras[nivel])
    return palabra
    

#Recibo una lista de palabras y selecciono una random
def obtenerPalabraAlAzar(listaDePalabras):
    palabraSeleccionada = random.choice(listaDePalabras)
    return palabraSeleccionada

#Recivo una palabra y la inserto en el archivo .csv de palabras.
def ingresarNuevasPalabras(nivel , palabraNueva):
    listPalabras = []
    seguirIngresando = False
    reader = csv.reader(open('ListaPalabras/ListaPalabras.csv'))
    for row in reader:
        listPalabras.append(row)
    responseValidate = validoPalabra(palabraNueva,listPalabras,nivel)
    if(responseValidate == False):
        return True
    else:
        listPalabras[nivel].append(palabraNueva)
        with open('ListaPalabras/ListaPalabras.csv','w' ,newline='') as file:
            writer = csv.writer(file)
            writer.writerows(listPalabras)
            msg = "Letra Ingresada Correctamente. ¿Desea Agregar Otra?"
            seguirIngresando = mb.askretrycancel(message=msg, title="Exitoo")
        return seguirIngresando
        
    

def validoPalabra(palabraNueva, listaPalabras, nivel):

    if(palabraNueva == ""):
        mb.showwarning(message="No ha ingresado ninguna palabra", title="!Atencion")
        return False
    ##Restricciones generales
    if(palabraNueva in listaPalabras):
        mb.showwarning(message="La palabra ingresada ya existe", title="!Atencion")
        return False
    numeros = "1234567890"
    for i in palabraNueva:
        if(i in numeros):
            mb.showwarning(message="La palabra solo debe contener Letras", title="!Atencion")
            return False 
    if(nivel == 0):
        if(len(palabraNueva) > 5):
            mb.showwarning(message="Las Palabras del nivel 1 deben tener como maximo 5 letras", title="!Atencion")
            return False
    if(nivel == 1):
        if(len(palabraNueva) > 9):
            mb.showwarning(message="Las Palabras del nivel 2 deben tener como maximo 9 letras", title="!Atencion")
            return False
    if(nivel == 2):
        if(len(palabraNueva) < 5 and len(palabraNueva) > 10 ):
            mb.showwarning(message="Las Palabras del nivel 3 deben tener como minimo 5 letras", title="!Atencion")
            return False

        
        


    
        