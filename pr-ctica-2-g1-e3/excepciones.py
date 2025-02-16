from tkinter import messagebox

class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"
    