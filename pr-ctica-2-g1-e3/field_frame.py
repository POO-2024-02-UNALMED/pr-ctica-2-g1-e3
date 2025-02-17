import tkinter as tk
import tkinter.ttk as ttk

class FieldFrame(tk.Frame):
    
    def __init__(self,ventana,tituloCriterios="",criterios=[],tituloValores="",valores=None,criteriosNoEditables=None, tipo = 0, comandoContinuar = None, comandoCancelar = None):
        super().__init__(ventana, width=400, height=300, bg='#1C2B2D')
        self._ventana = ventana
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._criteriosNoEditables = criteriosNoEditables
        self.tipo = tipo #0 para ingresar texto por el usuario, 1 para combobox, 2 para Si y No, 3 mostrar texto
        self.comandoContinuar= comandoContinuar
        self.comandoCancelar= comandoCancelar
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        

        #Datos que ingresa el usuario
        self._datos = []

        #Creación Título de Criterios
        self.labelTituloCriterios = tk.Label(self,text = self._tituloCriterios, fg="white", bg="#1C2B2D", font=("Segoe UI", 15, 'bold'))
        self.labelTituloCriterios.grid(row=0,column=0, padx=15,pady=10)

        #Creación Título de Valores
        self.labelTituloValores = tk.Label(self,text = self._tituloValores, fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
        self.labelTituloValores.grid(row=0,column=1, padx=15,pady=10)
        
        #Para ingresar texto por el usuario
        if tipo == 0:
            #Creación de columnas Valores y Criterios
            for i in range(len(self._criterios)):
                #Criterio
                labelCriterio = tk.Label(self,text=self._criterios[i], fg="white", bg="#1C2B2D", font=("Segoe UI", 15))
                labelCriterio.grid(row=i+1,column=0,padx=15,pady=15)
    
                #Valor
                entryValor = tk.Entry(self, width=30, font=("Segoe UI", 10))
                entryValor.grid(row=i+1,column=1,padx=15,pady=15,ipady=3)
    
                #Se ejecuta para establecer los valores predefinidos en el campo correspondiente
                if self._valores is not None:
                    if self._valores[i] is not None:
                        entryValor.insert(0,self._valores[i])
    
                if self._criteriosNoEditables is not None:
                    if self._criterios[i] in self._criteriosNoEditables:
                        entryValor.configure(state="readonly")
    
                self._datos.append(entryValor)

            
            # Creación del botón para guardar los datos
            btnGuardar = tk.Button(self, text="Continuar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=self.guardar_datos)
            btnGuardar.grid(row=len(criterios)+15, column=0, pady=15, columnspan=2)

        #Para combobox
        if tipo == 1:
            for i in range(len(self._criterios)):
                #Criterio
                labelCriterio = tk.Label(self,text=self._criterios[i], fg="white", bg="#1C2B2D", font=("Segoe UI", 15))
                labelCriterio.grid(row=i+1,column=0,padx=15,pady=15)
    
                #Valor
                entryValor = ttk.Combobox(self, values= self._valores[i],  state="readonly", font=("Segoe UI", 10), width=30)
                entryValor.set('Seleccione una opción')
                entryValor.bind("<<ComboboxSelected>>", self.on_select)
                entryValor.grid(row=i+1,column=1,padx=15,pady=15, ipady=3)
    
                #Se ejecuta para establecer los valores predefinidos en el campo correspondiente
                if self._valores is not None:
                    if self._valores[i] is not None:
                        entryValor.insert(0,self._valores[i])
    
                if self._criteriosNoEditables is not None:
                    if self._criterios[i] in self._criteriosNoEditables:
                        entryValor.configure(state="readonly")
    
                self._datos.append(entryValor)

            # Creación del botón para guardar los datos
            btnGuardar = tk.Button(self, text="Continuar",bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=self.guardar_datos)
            btnGuardar.grid(row=len(criterios)+15, column=0, pady=15, columnspan=2)

        #Para Si y No. El texto que se requiere mostrar se pone modificando _tituloCriterios
        if tipo == 2:
            botonSi = tk.Button(self, text='Sí',bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 20, "bold"), command= self.comandoContinuar)
            botonSi.grid(row = 1, column=0, padx=300, pady=10)
            botonNo = tk.Button(self, text='No',bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 20, "bold"), command=self.comandoCancelar)
            botonNo.grid(row = 1, column= 1, padx=300, pady=10)
            self.labelTituloCriterios.grid(columnspan=2)

        #El texto que se requiere mostrar se pone modificando _tituloCriterios
        if tipo == 3:
            texto = tk.Label(self, text= self._tituloCriterios, fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
            texto.grid(row= 0, column=0 ,columnspan=2, pady=15, sticky='new')


            
    
    def on_select(self, event):
        combobox = event.widget
        if combobox.get() == "↓↓ Escoja una opción ↓↓":
            combobox.set("")

    def obtener_datos(self):
        """Devuelve una lista con los valores ingresados por el usuario."""
        return [entry.get() for entry in self._datos]

    def guardar_datos(self):
        """Guarda los datos en self._valores y los imprime."""
        self._valores = self.obtener_datos()  # Guarda los datos actualizados
        print("Datos guardados:", self._valores)
        self.comandoContinuar()
        
    
    def get_value(self, criterio):
        """Devuelve el valor ingresado en el campo del criterio especificado."""
        if criterio in self._datos:
            return self._datos[criterio].get()
        return None  # Si el criterio no existe, devuelve None
        


# ---- Ejemplo de uso del FieldFrame ----

 #Crear la ventana principal
#root = tk.Tk()
#root.title("Prueba de FieldFrame")  # Título de la ventana
###
#### Definir criterios y valores
#criterios = ["Nombre:", "Numero Personas:", "Tipo de Mesa:"]
#valores = [['hola','olo'],['prueba','efwwe'],['gt','54']] #Predefinidos (Ingresarlos en el mismo orden que los criterios, colocar "None" para los que no tengran predefinidos)
#criteriosNoEditables = ["Nombre:"] #¿Cúales no puede editar el usuaio?
###
####Crear y agregar el FieldFrame a la ventana
#frame = FieldFrame(root, "Criterios", criterios, "Valores", valores,criteriosNoEditables, tipo=2)
#frame.pack(padx=15, pady=15)
###
###
###
#### Ejecutar la aplicación
###
###
#root.mainloop()