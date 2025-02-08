import tkinter as tk

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


ventana = tk.Tk()
ventana.title("Aura Gourmet System")
centrarVentana(ventana, 650, 650)

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
    "Nombre: NOMBRE1\nCédula: CEDULA1\nCarrera: CARRERA1\nNacimiento: FECHANACIMIENTO1",
    "Nombre: NOMBRE2\nCédula: CEDULA2\nCarrera: CARRERA2\nNacimiento: FECHANACIMIENTO2",
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
frameP1 = tk.Frame(ventana,bg="black")
frameP2 = tk.Frame(ventana,bg="#D4AF37")
frameP3 = tk.Frame(frameP1,bg="white")
frameP4 = tk.Frame(frameP1,bg="#2F4F4F")
frameP5 = tk.Frame(frameP2,bg="#2F4F4F")
frameP6 = tk.Frame(frameP2,bg="#2F4F4F")

#Creacion de los labels
labelP3 = tk.Label(frameP3,bg="#2F4F4F",fg="white",text="Bienvenidos(as)")
labelP4 = tk.Label(frameP4, bg="#2F4F4F", fg="white", text="hola", image=imagenes[0])
labelP5 = tk.Label(frameP5,bg="#2F4F4F",fg="white",text="Hojas de vida (Click para ver la primera)")

#PROVISIONAL PARA P6
labelP6 = tk.Frame(frameP6, bg="#2F4F4F")  # Contenedor de las secciones
secciones_p6 = [
    tk.Label(labelP6, bg="#2F4F4F", width=20, height=5),
    tk.Label(labelP6, bg="#2F4F4F", width=20, height=5),
    tk.Label(labelP6, bg="#2F4F4F", width=20, height=5),
    tk.Label(labelP6, bg="#2F4F4F", width=20, height=5),
]

# Distribuir las 4 secciones en una cuadrícula 2x2
secciones_p6[0].grid(row=0, column=0, sticky="nsew")
secciones_p6[1].grid(row=0, column=1, sticky="nsew")
secciones_p6[2].grid(row=1, column=0, sticky="nsew")
secciones_p6[3].grid(row=1, column=1, sticky="nsew")

# Expande cada celda en la cuadrícula
for i in range(2):
    labelP6.grid_rowconfigure(i, weight=1)
    labelP6.grid_columnconfigure(i, weight=1)

inicio = tk.Button(ventana,text="Inicio")

#Posicionamiento de los frames
frameP1.place(relx=0.02,rely=0.1,relwidth=0.47,relheight=0.85)
frameP2.place(relx=0.51,rely=0.1,relwidth=0.47,relheight=0.85)
frameP3.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP4.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)
frameP5.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP6.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)

labelP3.pack(expand=True,fill='both')
labelP4.pack(expand=True, fill='both')
labelP5.pack(expand=True, fill='both')
labelP6.pack(expand=True, fill='both')

# Asignar los eventos evento
labelP4.bind("<Enter>", EventoP4)
labelP5.bind("<Button-1>", EventoP5)

inicio.place(relx=0.02,rely=0.02)

ventana.mainloop()