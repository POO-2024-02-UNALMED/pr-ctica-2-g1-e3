import tkinter as tk
from field_frame import FieldFrame
from tkinter import messagebox

#Ubica la ventana en el centro de la pantalla
def centrarVentana(ventana, ancho, alto):
    # Obtiene las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    # Calcula las coordenadas para centrar la ventana
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2

    # Establece la geometría de la ventana
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#Muestra la ventana de dialogo acerca de
def acercaDe():
    messagebox.showinfo('Acerca de', 'Lo que queramos poner')

#Muestra la ventana de dialogo que explica de forma básica el sistema
def mensajeAplicacion():
    messagebox.showinfo('Acerca de Aura Gourmet System','Puedes navegar por las distintas funciones que te ofrece nuestro sistema para brindarte la posibilidad de realizar: Reservas, pedidos, domicilios, calificaciones y gestionar recompesas.')

#Cierra la ventana principal y serializa
def salir():
    #Serializar
    ventana.quit()

#Oculta ventana y muestra ventana2
def ventanaUsuario():
    ventana.withdraw()
    ventana2.deiconify()

#devuelve de la ventana2 a la ventana  
def salirMenuInicio():
    ventana2.withdraw()
    ventana.deiconify()

#Cambia el texto del labelP3 para describir el programa
def descripcionSistema():
    labelP3.config(text="Bienvenidos(as) al sistema de gestión\npara usuarios de Aura Gourmet."
                   + "\n\nEste sistema se encarga de proporcionar al cliente\nuna herramienta para realizar:"
                   + "\nReservas, domicilios, gestionar pedidos,\nrecompensas y calificaciones.", justify="left")
    
#Ventana inicio
ventana = tk.Tk()
ventana.title("Aura Gourmet System")
centrarVentana(ventana, 650, 650)
ventana.iconbitmap('pr-ctica-2-g1-e3/imagenes/logoRes.ico')
ventana.config(bg='#1E1E1E')

ventana2 = tk.Tk()
ventana2.title("Aura Gourmet System")
ventana2.iconbitmap('pr-ctica-2-g1-e3/imagenes/logoRes.ico')
centrarVentana(ventana2, 650, 650)
ventana2.config(bg='#1E1E1E')
ventana2.withdraw()


#Colores usados:
#Dorado oscuro:#D4AF37
#Negro:black
#Blanco:white
#Gris pizarra:#2F4F4F

# Cargar imágenes
imagenes = [
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante1.png"),
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante2.png"),
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante3.png"),
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante4.png"),
]
indice_imagen = 0  # Índice para alternar entre las imágenes

#Descripciones de los desarrolladores
descripciones = [
    "Nombre: Mateo Pérez\nCédula: 1000761827\nCarrera: Ingeniería de Sistemas\nNacimiento: 18/06/2003",
    "Nombre: Kevin Rubiano\nCédula: 1035417435\nCarrera: Ciencias de la computación\nNacimiento: 19/07/2005",
    "Nombre: Andrés Chica\nCédula: 1041351362\nCarrera: Ingeniería de sistemas e informática\nNacimiento: 24/04/2007",
    "Nombre: NOMBRE3\nCédula: CEDULA3\nCarrera: CARRERA3\nNacimiento: FECHANACIMIENTO3",
    "Nombre: NOMBRE4\nCédula: CEDULA4\nCarrera: CARRERA4\nNacimiento: FECHANACIMIENTO4",
]
indice_descripcion = 0  # Índice para alternar entre las descripciones

#PROVISIONAL DE PRUEBA PARA P6
colores_p6 = [
    ["red", "blue", "green", "yellow"],
    ["purple", "orange", "gray", "pink"],
    ["brown", "cyan", "white", "black"],
    ["#D4AF37", "#2F4F4F", "black", "white"],
    ["#D4AF37", "red", "orange", "yellow"],
]
indice_color = 0  # Índice para alternar entre colores

# Evento que modifica las 4 imagenes en el rectangulo inferior izquierdo
def EventoP4(evento):
    global indice_imagen
    nueva_imagen = imagenes[indice_imagen]
    labelP4.config(image=nueva_imagen)
    indice_imagen = (indice_imagen + 1) % len(imagenes)  # Alternar entre las 

# Evento para cambiar la descripción en labelP5 Y PROVISIONAL PARA P6
def EventoP5(evento):
    global indice_descripcion, indice_color

    # Cambia la descripción de labelP5
    labelP5.config(text=descripciones[indice_descripcion])
    indice_descripcion = (indice_descripcion + 1) % len(descripciones)

    # Cambia los colores de las secciones de labelP6
    colores_actuales = colores_p6[indice_color]
    for i in range(4):
        secciones_p6[i].config(bg=colores_actuales[i])
    
    indice_color = (indice_color + 1) % len(colores_p6)
    

#Creacion de los frames
frameP1 = tk.Frame(ventana,bg="#2D2D2D")
frameP2 = tk.Frame(ventana,bg="#2D2D2D")
frameP3 = tk.Frame(frameP1,bg="white")
frameP4 = tk.Frame(frameP1,bg="#1C2B2D")
frameP5 = tk.Frame(frameP2,bg="#1C2B2D")
frameP6 = tk.Frame(frameP2,bg="#1C2B2D")

#Creacion de los labels
labelP3 = tk.Label(frameP3,bg="#1C2B2D",fg="white",text="Bienvenidos(as) al sistema de gestión \n para usuarios de Aura Gourmet.")
labelP4 = tk.Label(frameP4, bg="#1C2B2D", fg="white", text="hola", image=imagenes[0])
labelP5 = tk.Label(frameP5,bg="#1C2B2D",fg="white",text="Hojas de vida (Click para cambiar)", justify="left")

#PROVISIONAL PARA P6
labelP6 = tk.Frame(frameP6, bg="#1C2B2D")  # Contenedor de las secciones
secciones_p6 = [
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
]

# Creación de los botones
buttonP4 = tk.Button(frameP4,text="Entrar",width=20,height=3, relief="solid", bd=3, font=("Arial", 10, "bold"), command=ventanaUsuario)

# Distribuir las 4 secciones en una cuadrícula 2x2
secciones_p6[0].grid(row=0, column=0, sticky="nsew")
secciones_p6[1].grid(row=0, column=1, sticky="nsew")
secciones_p6[2].grid(row=1, column=0, sticky="nsew")
secciones_p6[3].grid(row=1, column=1, sticky="nsew")

# Expande cada celda en la cuadrícula
for i in range(2):
    labelP6.grid_rowconfigure(i, weight=1)
    labelP6.grid_columnconfigure(i, weight=1)

#Menu inicio
menuInicio = tk.Menu(ventana)
subMenuInicio = tk.Menu(menuInicio, tearoff=0, activebackground='#1C2B2D')
subMenuInicio.add_cascade(label = 'Descripción del sistema', command= descripcionSistema)
subMenuInicio.add_cascade(label = 'Salir', command=salir)
menuInicio.add_cascade(label='Inicio', menu= subMenuInicio)
ventana.config(menu= menuInicio)

#Menu ventana usuario
menuUsuario = tk.Menu(ventana2)
subMenuUsuario1 = tk.Menu(menuUsuario, tearoff=0, activebackground='#1C2B2D')
subMenuUsuario1.add_cascade(label = 'Aplicación', command=mensajeAplicacion)
subMenuUsuario1.add_cascade(label = 'Salir', command=salirMenuInicio)
menuUsuario.add_cascade(label='Archivo', menu=subMenuUsuario1)
subMenuUsuario2 = tk.Menu(menuUsuario, tearoff=0, activebackground='#1C2B2D')
subMenuUsuario2.add_cascade(label = 'Realizar una reserva')
subMenuUsuario2.add_cascade(label = 'Realizar un domicilio')
subMenuUsuario2.add_cascade(label = 'Realizar el pedido de mi reserva')
subMenuUsuario2.add_cascade(label = 'Gestionar recompensas')
subMenuUsuario2.add_cascade(label = 'Calificar el servicio')
menuUsuario.add_cascade(label = 'Procesos y consultras', menu=subMenuUsuario2)
subMenuUsuario3 = tk.Menu(menuUsuario, tearoff=0, activebackground='#1C2B2D')
subMenuUsuario3.add_cascade(label = 'Acerca de', command=acercaDe)
menuUsuario.add_cascade(label = 'Ayuda', menu=subMenuUsuario3)
ventana2.config(menu= menuUsuario)

#Posicionamiento de los frames
frameP1.place(relx=0.02,rely=0.1,relwidth=0.47,relheight=0.85)
frameP2.place(relx=0.51,rely=0.1,relwidth=0.47,relheight=0.85)
frameP3.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP4.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)
frameP5.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP6.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)

labelP3.pack(expand=True,fill='both')
labelP4.pack(side='top', fill='x')
labelP5.pack(expand=True, fill='both')
labelP6.pack(expand=True, fill='both')

buttonP4.pack(side='bottom',expand = True)

# Asignar los eventos evento
labelP4.bind("<Enter>", EventoP4)
labelP5.bind("<Button-1>", EventoP5)

ventana.mainloop()