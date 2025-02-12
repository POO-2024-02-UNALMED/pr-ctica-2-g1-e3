import tkinter as tk

class FieldFrame(tk.Frame):
    
    def __init__(self,ventana,tituloCriterios="",criterios=[],tituloValores="",valores=None,criteriosNoEditables=None):
        super().__init__(ventana)
        self._ventana = ventana
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._criteriosNoEditables = criteriosNoEditables

        #Datos que ingresa el usuario
        self._datos = []

        #Creación Título de Criterios
        self.labelTituloCriterios = tk.Label(self,text = self._tituloCriterios)
        self.labelTituloCriterios.grid(row=0,column=0, padx=15,pady=15)

        #Creación Título de Valores
        self.labelTituloValores = tk.Label(self,text = self._tituloValores)
        self.labelTituloValores.grid(row=0,column=1, padx=15,pady=15)
        
        #Creación de columnas Valores y Criterios
        for i in range(len(self._criterios)):
            #Criterio
            labelCriterio = tk.Label(self,text=self._criterios[i])
            labelCriterio.grid(row=i+1,column=0,padx=15,pady=15)

            #Valor
            entryValor = tk.Entry(self)
            entryValor.grid(row=i+1,column=1,padx=15,pady=15)

            #Se ejecuta para establecer los valores predefinidos en el campo correspondiente
            if self._valores is not None:
                if self._valores[i] is not None:
                    entryValor.insert(0,self._valores[i])

            if self._criteriosNoEditables is not None:
                if self._criterios[i] in self._criteriosNoEditables:
                    entryValor.configure(state="readonly")

            self._datos.append(entryValor)
        
        # Creación del botón para guardar los datos
        btnGuardar = tk.Button(self, text="Aceptar", command=self.guardar_datos)
        btnGuardar.grid(row=len(criterios)+15, column=1, pady=15)
    
    def obtener_datos(self):
        """Devuelve una lista con los valores ingresados por el usuario."""
        return [entry.get() for entry in self._datos]

    def guardar_datos(self):
        """Guarda los datos en self._valores y los imprime."""
        self._valores = self.obtener_datos()  # Guarda los datos actualizados
        print("Datos guardados:", self._valores)
    
    def get_value(self, criterio):
        """Devuelve el valor ingresado en el campo del criterio especificado."""
        if criterio in self._datos:
            return self._datos[criterio].get()
        return None  # Si el criterio no existe, devuelve None
        


# ---- Ejemplo de uso del FieldFrame ----

# Crear la ventana principal
#root = tk.Tk()
#root.title("Prueba de FieldFrame")  # Título de la ventana

# Definir criterios y valores
#criterios = ["Nombre:", "Numero Personas:", "Tipo de Mesa:"]
#valores = ["Andres",None,"basic"] #Predefinidos (Ingresarlos en el mismo orden que los criterios, colocar "None" para los que no tengran predefinidos)
#criteriosNoEditables = ["Nombre:"] #¿Cúales no puede editar el usuaio?

# Crear y agregar el FieldFrame a la ventana
#frame = FieldFrame(root, "Criterios", criterios, "Valores", valores,criteriosNoEditables)
#frame.pack(padx=15, pady=15)

# Ejecutar la aplicación
#root.mainloop()