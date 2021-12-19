import tkinter
from tkinter import filedialog
import xml.etree.ElementTree as ET

  #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------- Listas --------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------- XML --------------------------------------------------------
from ListaDoble import *
Artista_Lista = ListaDobleArtista()

Listar = Llenado()

def buscador():
    val = filedialog.askopenfilename(title ='Seleccion de archivo xml',initialdir = './', filetypes=(('xml files', '*.xml'),('all files','*.*')))
    cargaXML(val)
  
def cargaXML(ruta):   
    contenido = open(ruta).read()
    biblioteca = ET.fromstring(contenido)
    for biblio in biblioteca.iter("biblioteca"):
        for can in biblio.iter("cancion"):
            nombre = can.attrib['nombre']
            album = ""
            artista = ""
            imagen = ""
            ruta = ""
            for ar in can.iter("artista"):
                artista += ar.text  
            for al in can.iter("album"):
                album += al.text  
            for im in can.iter("imagen"):
                imagen += im.text 
            for ru in can.iter("ruta"):
                ruta += ru.text   
            Listar.agregarCancion(artista,album,imagen,ruta,nombre)
 


class IG():   

    ventana =  tkinter.Tk()
    ventana.title("IPCmusic")
    ventana.geometry("1100x700")
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------ Frames ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    frame = tkinter.Frame(ventana)
    # Establece la posición del componente
    frame.place(x=35,y=85)
    # Color de fondo, background
    frame.config(bg="lightgrey")   
    # Podemos establecer un tamaño
    frame.config(width=1000,height=550)
    # Establece el ancho del borde 
    frame.config(bd=10)
    # Establece el tipo de relieve para el borde
    frame.config(relief="ridge")

    frameInfo = tkinter.Frame(frame)
    # Establece la posición del componente
    frameInfo.place(x=400,y=150)
    # Color de fondo, background
    frameInfo.config(bg="grey")   
    # Podemos establecer un tamaño
    frameInfo.config(width=500,height=250)
    # Establece el ancho del borde 
    frameInfo.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameInfo.config(relief="ridge")

    frameAr = tkinter.Frame(ventana)
    # Establece la posición del componente
    frameAr.place(x=35,y=10)
    # Color de fondo, background
    frameAr.config(bg="lightgrey")   
    # Podemos establecer un tamaño
    frameAr.config(width=400,height=60)
    # Establece el ancho del borde 
    frameAr.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameAr.config(relief="ridge")

    frameBu = tkinter.Frame(ventana)
    # Establece la posición del componente
    frameBu.place(x=450,y=10)
    # Color de fondo, background
    frameBu.config(bg="lightgrey")   
    # Podemos establecer un tamaño
    frameBu.config(width=585,height=60)
    # Establece el ancho del borde 
    frameBu.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameBu.config(relief="ridge")

    frameIm = tkinter.Frame(frame)
    # Establece la posición del componente
    frameIm.place(x=55,y=65)
    # Color de fondo, background
    frameIm.config(bg="grey")   
    # Podemos establecer un tamaño
    frameIm.config(width=300,height=400)
    # Establece el ancho del borde 
    frameIm.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameIm.config(relief="ridge")

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------ Labels ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    Label1 = tkinter.Label(frameInfo, text="Canción")
    Label1.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label1.place(x=10,y=40)

    CANCION = "VALOR"

    Label1A = tkinter.Label(frameInfo, text=CANCION)
    Label1A.config(fg="white", bg="grey", font=("broadway 15 "))
    Label1A.place(x=150,y=45)

    Label2 = tkinter.Label(frameInfo, text="Artista")
    Label2.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label2.place(x=10,y=90)

    ARTISTA = "VALOR2"

    Label2A = tkinter.Label(frameInfo, text=ARTISTA)
    Label2A.config(fg="white", bg="grey", font=("broadway 15"))
    Label2A.place(x=150,y=95)

    Label3 = tkinter.Label(frameInfo, text="Album")
    Label3.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label3.place(x=10,y=140)

    ALBUM = "VALOR3"

    Label3A = tkinter.Label(frameInfo, text=ALBUM)
    Label3A.config(fg="white", bg="grey", font=("broadway 15"))
    Label3A.place(x=150,y=145)

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------ Buttons --------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    
    def hola():
        print("Hola Mundo")  

    

    img = tkinter.PhotoImage(file='anterior.png')
    img_label = tkinter.Label(image=img)
    boton1 = tkinter.Button(frame, image=img, command = hola, borderwidth=0, bg="lightgrey")
    boton1.place(x=500,y=420)
    boton1.config(width=75, height=75)

    img2 = tkinter.PhotoImage(file='siguiente.png')
    img_label2 = tkinter.Label(image=img2)
    boton2 = tkinter.Button(frame, image=img2, command = hola, borderwidth=0, bg="lightgrey")
    boton2.place(x=700,y=420)
    boton2.config(width=75, height=75)

    img3 = tkinter.PhotoImage(file='play.png')
    img_label3 = tkinter.Label(image=img3)
    boton3 = tkinter.Button(frame, image=img3, command = hola, borderwidth=0, bg="lightgrey")
    boton3.place(x=500,y=50)
    boton3.config(width=75, height=75)

    img4 = tkinter.PhotoImage(file='pausa.png')
    img_label4 = tkinter.Label(image=img4)
    boton4 = tkinter.Button(frame, image=img4, command = hola, borderwidth=0, bg="lightgrey")
    boton4.place(x=600,y=50)
    boton4.config(width=75, height=75)

    img5 = tkinter.PhotoImage(file='stop.png')
    img_label5 = tkinter.Label(image=img5)
    boton5 = tkinter.Button(frame, image=img5, command = hola, borderwidth=0, bg="lightgrey")
    boton5.place(x=700,y=50)
    boton5.config(width=75, height=75)
    
    boton6 = tkinter.Button(frameAr,text="Archivo", fg="white",font=("broadway 12 bold"), command = buscador, borderwidth=0, bg="grey")
    boton6.place(x=25,y=5)
    boton6.config(width=12, height=1)

    boton7 = tkinter.Button(frameAr,text="Reporte", fg="white",font=("broadway 12 bold"), command = Listar.graphviz, borderwidth=0, bg="grey")
    boton7.place(x=205,y=5)
    boton7.config(width=12, height=1)

    busqueda = tkinter.StringVar()
    txtA = tkinter.Entry(frameBu, textvariable=busqueda)
    txtA.place(x=43,y=0)
    txtA.config(width=86)
    
    
    def pn(valor):        
        print(valor)

    img8 = tkinter.PhotoImage(file='lupa.png')
    img_label8 = tkinter.Label(image=img8)
    boton8 = tkinter.Button(frameBu, image=img8, command = pn(busqueda.get()), borderwidth=0, bg="white")
    boton8.place(x=0,y=0)
    boton8.config(width=40, height=40)

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------- Entry ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------  
    #-----------------------------------------------------------------------------------------------------------------------      

    ventana.config(cursor="arrow")
    ventana.config(bg="grey")
    ventana.config(bd=15)
    ventana.config(relief="ridge")
    ventana.mainloop() 

