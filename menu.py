import tkinter as tk
from PIL import ImageTk, Image
import manejoArchivo as mArch
import ahorcado as juego
from tkinter import ttk 

images_list = []
palabras = ""
palabraSecreta = ""
letrasIncorrectas = ""
letrasCorrectas = ""
intentosIncorrectos = 0
letraIngresada = ''
newWindow = ""
myImage = ""
myLabelPalabra = ""
botonArriesgar = ""
combo = ""
windowNivel = ""
#Por defecto el nivel siempre es 0
nivel = 0
comboNewWord= ""
entrynewWord = ""
windowNewWord = ""


def __init__():  
    global images_list 
    global palabraSecreta
    ventana1 = tk.Tk()
    ventana1.geometry('300x150')
    ventana1.title("Menu Inicio")
    ventana1['bg'] = '#49A'
    ventana1.iconbitmap('IconosSistema/superman.ico')
    menubar1 = tk.Menu(ventana1)
    my_img = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado1.jpeg").resize((150, 150)))
    my_img1 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado2.jpeg").resize((150, 150)))
    my_img2 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado3.jpeg").resize((150, 150)))
    my_img3 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado4.jpeg").resize((150, 150)))
    my_img4 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado5.jpeg").resize((150, 150)))
    my_img5 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado6.jpeg").resize((150, 150)))
    my_img6 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado7.jpeg").resize((150, 150)))
    my_img7 = ImageTk.PhotoImage(Image.open(
        "ImagenesAhorcado/Ahorcado8.jpeg").resize((150, 150)))
    images_list = [my_img, my_img1, my_img2,
                   my_img3, my_img4, my_img5, my_img6, my_img7]

    ventana1.config(menu=menubar1)
    opciones1 = tk.Menu(menubar1)
    opciones1.add_command(label="Nuevo", command=seleccionarNivel )
    opciones1.add_command(label="Salir", command=ventana1.quit)
    menubar1.add_cascade(label="Archivo", menu=opciones1)
    opciones2 = tk.Menu(menubar1)
    opciones2.add_command(label="Regla de Juego", command =mostrarReglasJuego)
    menubar1.add_cascade(label="Ayuda", menu=opciones2)
    botonInitGame = tk.Button(ventana1, text="Iniciar Juego", command=seleccionarNivel)
    botonMoreWords = tk.Button(ventana1, text="Ingresar mas Palabras", command=agregarNuevaLetra)
    botonInitGame.pack()
    botonInitGame.pack()
    botonInitGame.place(x=30, y=20)
    botonMoreWords.place(x=130, y=20)
    ventana1.mainloop()


def seleccionarNivel():
    global combo
    global nivel
    global windowNivel
    windowNivel = tk.Toplevel()
    windowNivel.title("Seleccione un Nivel")
    windowNivel.geometry('300x150')
    windowNivel['bg'] = '#FFFFFF'
    windowNivel.iconbitmap('IconosSistema/superman.ico')
    labelCombo = tk.Label(windowNivel,text= "¿En que nivel desea jugar?")
    labelCombo.pack()
    combo =  tk.ttk.Combobox(windowNivel, values = ["Nivel 1", "Nivel 2", "Nivel 3"] )
    combo.current(0)
    combo.bind("<<ComboboxSelected>>", callback)
    combo.pack()
    botonArriesgar = tk.Button(windowNivel, text="¡Jugar!",borderwidth = 5 , command= createNewWindow)
    botonArriesgar.pack()

def callback(eventObject):
    global combo
    global nivel
    nivelSelected = combo.get()
    if(nivelSelected == "Nivel 2"):
        nivel = 1
    elif(nivelSelected == "Nivel 3"):
        nivel = 2

def createNewWindow():
    global images_list
    global palabraSecreta
    global letrasIncorrectas
    global letrasCorrectas
    global intentosIncorrectos
    global letraIngresada
    global myImage
    global myLabelPalabra
    global newWindow
    global botonArriesgar
    global windowNivel
    
    #Cierro la ventana del nivel
    windowNivel.destroy()
    #Selecciono la palabra segun el nivel Seleccionado
    palabraSecreta = mArch.seleccionoPalabrasPorNivel(nivel)
    newWindow = tk.Toplevel()
    newWindow.title("Bienvenidos al Ahorcado")
    newWindow.geometry('350x350')
    newWindow['bg'] = '#FFFFFF'
    newWindow.iconbitmap('IconosSistema/superman.ico')
    myImage = tk.Label(newWindow, image=images_list[intentosIncorrectos])
    myImage['bg'] = '#FFFFFF'
    myImage.pack()
    #Relleno el textBox con "_"
    myLabelPalabra = tk.Label(newWindow, text= juego.letraOculta(palabraSecreta,letrasCorrectas) )
    myLabelPalabra.config(fg="blue",font=("Verdana",18)) 
    myLabelPalabra['bg'] = '#FFFFFF'
    myLabelPalabra.pack()
    letraIngresada = tk.Entry(newWindow, borderwidth = 5)
    letraIngresada.focus()
    # Posicionarla en la ventana.
    letraIngresada.pack()
    botonArriesgar = tk.Button(newWindow, text="!Arriesgar",borderwidth = 5 , command= arriegaLetra)
    botonArriesgar.pack()
    

    
def arriegaLetra():
    global images_list
    global palabraSecreta
    global letrasIncorrectas
    global letrasCorrectas
    global intentosIncorrectos
    global letraIngresada
    global newWindow
    global myImage
    global myLabelPalabra
    global botonArriesgar

    nuevaletra = letraIngresada.get()
    cerrarVentana = False
    if(letraIngresada != ''):
        if(juego.validoIntento(nuevaletra, letrasCorrectas+letrasIncorrectas)):
            mensajeResponse = juego.jugada(nuevaletra,palabraSecreta,letrasCorrectas,letrasIncorrectas, images_list)
            if(mensajeResponse == "letraIncorrecta"):
                letrasIncorrectas = letrasIncorrectas + nuevaletra
                intentosIncorrectos = intentosIncorrectos + 1
            elif(mensajeResponse == "letraCorrecta"):
                letrasCorrectas = letrasCorrectas + nuevaletra
            elif(mensajeResponse == "juegoGanado" or mensajeResponse == "juegoPerdido" ):
                letrasIncorrectas = ""
                letrasCorrectas = ""
                intentosIncorrectos = 0
                cerrarVentana = True
            elif(mensajeResponse == "seguirJugando"):
                letrasIncorrectas = ""
                letrasCorrectas = ""
                intentosIncorrectos = 0
                palabraSecreta = mArch.seleccionoPalabrasPorNivel(nivel)

    #Elimino los labes ya exitentes para actualizarlos.
    myLabelPalabra.forget()
    myImage.forget()
    letraIngresada.forget()
    botonArriesgar.forget()
    myImage = tk.Label(newWindow, image=images_list[intentosIncorrectos])
    myImage['bg'] = '#FFFFFF'
    myImage.pack()
    #Relleno el textBox con "_"
    myLabelPalabra = tk.Label(newWindow, text= juego.letraOculta(palabraSecreta,letrasCorrectas) )
    myLabelPalabra.config(fg="blue",font=("Verdana",18)) 
    myLabelPalabra['bg'] = '#FFFFFF'
    myLabelPalabra.pack()
    letraIngresada = tk.Entry(newWindow, borderwidth = 5)
    letraIngresada.focus()
    # Posicionarla en la ventana.
    letraIngresada.pack()
    botonArriesgar = tk.Button(newWindow, text="!Arriesgar",borderwidth = 5 , command= arriegaLetra)
    botonArriesgar.pack()
    if(cerrarVentana):
        newWindow.destroy()
   
def mostrarReglasJuego():
    windowReglas = tk.Toplevel()
    windowReglas.title("Reglas de Juego")
    windowReglas.geometry('650x200')
    windowReglas['bg'] = '#FFFFFF'
    windowReglas.iconbitmap('IconosSistema/superman.ico')
    archivo = open('Reglas/ReglasAhorcado.txt', 'r')
    labelExample = tk.Label(windowReglas, text=archivo.read())
    labelExample['bg'] = '#FFFFFF'
    archivo.close()
    labelExample.pack()


def agregarNuevaLetra():
    global windowNewWord
    global comboNewWord
    global entrynewWord
    windowNewWord = tk.Toplevel()
    windowNewWord.title("Agregar Nueva Palabra")
    windowNewWord.geometry('300x150')
    windowNewWord['bg'] = '#FFFFFF'
    windowNewWord.iconbitmap('IconosSistema/superman.ico')
    labelComboNewWord = tk.Label(windowNewWord,text= "Seleccione un nivel:")
    labelComboNewWord.pack()
    comboNewWord =  tk.ttk.Combobox(windowNewWord, values = ["Nivel 1", "Nivel 2", "Nivel 3"])
    comboNewWord.current(0)
    comboNewWord.pack()
    entrynewWord = tk.Entry(windowNewWord, borderwidth = 5)
    entrynewWord.focus()
    entrynewWord.pack()
    botonIngresar = tk.Button(windowNewWord, text="Ingresar",borderwidth = 5 , command= validateWord)
    botonIngresar.pack()

def validateWord():
    global windowNewWord
    global comboNewWord
    global entrynewWord

    nivelSeleccionado = 0

    if(comboNewWord.get() == "Nivel 2"):
        nivelSeleccionado = 1
    elif(comboNewWord.get() == "Nivel 3"):
        nivelSeleccionado = 2
    seguirIngresando = mArch.ingresarNuevasPalabras(nivelSeleccionado,entrynewWord.get())
    if(seguirIngresando):
        windowNewWord.destroy()
        agregarNuevaLetra()
    else:
       windowNewWord.destroy() 


    
__init__()