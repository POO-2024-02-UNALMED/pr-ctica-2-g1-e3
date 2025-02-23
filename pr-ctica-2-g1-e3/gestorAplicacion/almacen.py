from .menu import Menu

class Almacen:
    _almacen = []

    def __init__(self):
        self._nombres = []
        self._cantidades = []
        self._inicializar_inventario()
        Almacen._almacen.append(self)

    def _inicializar_inventario(self):
        self.agregar_producto("salmon", 5)
        self.agregar_producto("cordero", 5)
        self.agregar_producto("langosta", 5)
        self.agregar_producto("mantequilla", 10)
        self.agregar_producto("limon", 8)
        self.agregar_producto("pasta", 15)
        self.agregar_producto("tomate", 20)
        self.agregar_producto("albahaca", 10)
        self.agregar_producto("hierbas finas", 12)
        self.agregar_producto("aceite de oliva", 18)
        self.agregar_producto("ajo", 14)
        self.agregar_producto("pulpo", 4)
        self.agregar_producto("pimenton", 7)
        self.agregar_producto("lomo de buey", 5)
        self.agregar_producto("sal", 25)
        self.agregar_producto("pimienta", 20)
        self.agregar_producto("atun", 9)
        self.agregar_producto("aguacate", 8)
        self.agregar_producto("salsa de soya", 10)
        self.agregar_producto("ravioli", 6)
        self.agregar_producto("trufa", 5)
        self.agregar_producto("queso parmesano", 15)

    def agregar_producto(self, nombre, cantidad):
        if nombre in self._nombres:
            index = self._nombres.index(nombre)
            self._cantidades[index] += cantidad
        else:
            self._nombres.append(nombre)
            self._cantidades.append(cantidad)

    def verificar_disponibilidad(self, menu):
        for ingrediente in menu.get_ingredientes():
            if ingrediente not in self._nombres or self._cantidades[self._nombres.index(ingrediente)] <= 0:
                return False
        return True

    def sugerir_menus(self):
        menus_sugeridos = []
        for menu in Menu.values():
            if self.verificar_disponibilidad(menu):
                menus_sugeridos.append(menu.nombre)
        return menus_sugeridos

    def mostrar_inventario(self):
        print("Inventario actual:")
        for i in range(len(self._nombres)):
            print(f"Producto: {self._nombres[i]}, Cantidad: {self._cantidades[i]}")

    def preparar_menu(self, menu):
        if self.verificar_disponibilidad(menu):
            for ingrediente in menu.ingredientes:
                index = self._nombres.index(ingrediente)
                self._cantidades[index] -= 1
            return True
        else:
            print(f"No hay suficientes ingredientes para preparar {menu.nombre}")
            return False

    @staticmethod
    def get_almacen():
        return Almacen._almacen

    def actualizar_inventario(self, menu, cantidad):
        for ingrediente in menu.ingredientes:
            if ingrediente in self._nombres:
                index = self._nombres.index(ingrediente)
                self._cantidades[index] -= cantidad

    def revertir_inventario(self, menu, cantidad):
        for ingrediente in menu.ingredientes:
            if ingrediente in self._nombres:
                index = self._nombres.index(ingrediente)
                self._cantidades[index] += cantidad
