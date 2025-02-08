import tkinter as tk

ventana = tk.Tk()
ventana.geometry("650x650")
ventana.title("Aura Gourmet System")

#Colores usados:
#Dorado oscuro:#D4AF37
#Negro:black
#Blanco:white
#Gris pizarra:#2F4F4F

frameP1 = tk.Frame(ventana,bg="black")
frameP2 = tk.Frame(ventana,bg="#D4AF37")
frameP3 = tk.Frame(frameP1,bg="white")
frameP4 = tk.Frame(frameP1,bg="#2F4F4F")
frameP5 = tk.Frame(frameP2,bg="#2F4F4F")
frameP6 = tk.Frame(frameP2,bg="#2F4F4F")

labelP3 = tk.Label(frameP3,bg="#2F4F4F",fg="white",text="Bienvenidos(as)")
inicio = tk.Button(ventana,text="Inicio")

frameP1.place(relx=0.02,rely=0.1,relwidth=0.47,relheight=0.85)
frameP2.place(relx=0.51,rely=0.1,relwidth=0.47,relheight=0.85)
frameP3.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP4.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)
frameP5.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP6.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)

labelP3.pack(expand=True,fill='both')
inicio.place(relx=0.02,rely=0.02)

ventana.mainloop()