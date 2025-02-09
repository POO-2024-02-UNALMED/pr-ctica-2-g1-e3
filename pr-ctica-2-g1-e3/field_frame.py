import tkinter as tk

class FieldFrame(tk.Frame):
    
    def __init__(self,ventana,tituloCriterios="",criterios=[],tituloValores="",valores=None,valoresDefault=None):
        super().__init__(ventana)
        self._ventana = ventana
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._valoresDefault = valoresDefault

        #Datos que ingresa el usuario
        self._datos = []

        #Creación Columna de Criterios
        self.labelTituloCriterios = tk.Label(self,text = self._tituloCriterios)
        self.labelTituloCriterios.grid(row=0,column=0, padx=50,pady=50)

        #Creación Columna de Valores
        self.labelTituloValores = tk.Label(self,text = self._tituloValores)
        self.labelTituloValores.grid(row=0,column=1, padx=50,pady=50)
        
        for i in range(len(self._criterios)):
            labelCriterio = tk.Label(self,text=self._criterios[i])
            labelCriterio.grid(row=i+1,column=0,padx=50,pady=50)

        for i in range(len(self._valores)):
            entryValor = tk.Entry(self)
            entryValor.grid(row=i+1,column=1,padx=50,pady=50)

# ---- Prueba de FieldFrame ----

# Crear la ventana principal
root = tk.Tk()
root.title("Prueba de FieldFrame")  # Título de la ventana

# Definir criterios y valores
criterios = ["Nombre:", "Numero Personas:", "Tipo de Mesa:"]
valores = [None]*3

# Crear y agregar el FieldFrame a la ventana
frame = FieldFrame(root, "Criterios", criterios, "Valores", valores)
frame.pack(padx=20, pady=20)

# Ejecutar la aplicación
root.mainloop()