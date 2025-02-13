import locale

class Utilidad:
    @staticmethod
    def solicitar_entero(x, y):
        while True:
            try:
                numero = int(input(f"Ingresa un número entre {x} y {y}: "))
                if x <= numero <= y:
                    return numero
                else:
                    print("El número no está en el rango permitido. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero en el rango establecido.")
    
    @staticmethod
    def solicitar_id():
        while True:
            try:
                numero = int(input("Ingrese su identificación para realizar la calificación: "))
                return numero
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número válido.")
    
    @staticmethod
    def formato_precio(precio):
        locale.setlocale(locale.LC_ALL, '')
        return locale.currency(precio, grouping=True)
    
    @staticmethod
    def aplicar_descuento(calificacion, total_factura):
        if calificacion is not None:
            promedio = calificacion.get_promedio_calificacion()
            descuento = 0
            
            if promedio <= 2:
                descuento = 10  # 10% de descuento
            elif promedio <= 3:
                descuento = 5  # 5% de descuento

            total_factura -= (total_factura * descuento) / 100
            
            return f"Total: {total_factura}\nDescuento aplicado: {descuento}% de descuento"
        
        return None