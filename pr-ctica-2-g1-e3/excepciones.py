from tkinter import messagebox

class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"
    
class ValidacionDatos(ErrorAplicacion):
    def __init__(self, mensaje_error_hijo):
        if mensaje_error_hijo is not None:
            self.mensaje_error_inicio = f"Ha ocurrido un error: {mensaje_error_hijo}"
        else:
            self.mensaje_error_inicio = "Ha ocurrido un error"
        super().__init__(self.mensaje_error_inicio)
    
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"

class IdNoEncontrado(ValidacionDatos):
    def __init__(self, id):
        self.mensaje_error_valor = f"la identificación: {id} no se encuentra en el sistema."
        messagebox.showerror("Error: Identificación no encontrada", self.mensaje_error_valor)
        super().__init__(self.mensaje_error_valor)

class HoraInvalida(ValidacionDatos):
    def __init__(self, hora):
        self.mensaje_error_valor = f"La hora ({hora}) ingresada no tiene el formato correcto.\nej: 17:30"
        messagebox.showerror("Error: Formato incorrecto", self.mensaje_error_valor)
        super().__init__(self.mensaje_error_valor)

class FechaInvalida(ValidacionDatos):
    def __init__(self, fecha):
        self.mensaje_error_valor = f"La fecha ({fecha}) ingresada no tiene el formato correcto.\nej: 22/02/2025"
        messagebox.showerror("Error: Formato incorrecto", self.mensaje_error_valor)
        super().__init__(self.mensaje_error_valor)

class DireccionErrronea(ValidacionDatos):
    def __init__(self, direccion):
        self.mensaje_error_valor = f"La dirección ({direccion} ingresada no tiene el formato correcto. ej : Calle 45 # 32)"
        messagebox.showerror("Error: Formato incorrecto", self.mensaje_error_valor)
        super().__init__(self.mensaje_error_valor)

class DatosEntrada(ErrorAplicacion):
    def __init__(self, mensaje_error_hijo):
        if mensaje_error_hijo is not None:
            self.mensaje_error_inicio = f"Ha ocurrido un error en el Entry: {mensaje_error_hijo}"
            messagebox.showerror("Error: Datos erróneos", self.mensaje_error_inicio)
        else:
            self.mensaje_error_inicio = "Ha ocurrido un error en el Entry"
        super().__init__(self.mensaje_error_inicio)
    
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"

class EntryVacio(DatosEntrada):
    def __init__(self, entryVacio):
        self.mensaje_error = f"El siguiente campo está vacio: {entryVacio}"
        messagebox.showerror("Error: Selección vacía", self.mensaje_error)
        super().__init__(self.mensaje_error)

class BoxVacio(DatosEntrada):
    def __init__(self, BoxVacio):
        self.mensaje_error = f"El siguiente campo está vacio: {BoxVacio}"
        messagebox.showerror("Error: Selección vacía", self.mensaje_error)
        super().__init__(self.mensaje_error)

class ExcepcionTipoMesa(DatosEntrada):
    def __init__(self, MesaIngresada):
        self.mensaje_error = f"El tipo de mesa ({MesaIngresada} es incorrecto.\n(Debe ser 'deluxe' o 'basic'))"
        messagebox.showerror("Error: Formatoincorrecto", self.mensaje_error)
        super().__init__(self.mensaje_error)

class IdEntryNoNumerico(DatosEntrada):
    def __init__(self, idNoNumerico):
        self.mensaje_error = f"El valor ({idNoNumerico}) es incorrecto"
        messagebox.showerror("Error: Formato incorrecto", self.mensaje_error)
        super().__init__(self.mensaje_error)









