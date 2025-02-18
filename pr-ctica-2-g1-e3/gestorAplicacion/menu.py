from enum import Enum

class Menu(Enum):
    LANGOSTA = ("Langosta", 120000, ["langosta", "mantequilla", "limon"])
    SALMON_AHUMADO = ("Salmón Ahumado", 85000, ["salmon", "hierbas finas", "aceite de oliva"])
    CORDERO = ("Cordero", 95000, ["cordero", "hierbas finas", "ajo"])
    PULPO_A_LA_GALLEGA = ("Pulpo a la Gallega", 110000, ["pulpo", "pimenton", "aceite de oliva"])
    PASTA_FRESCA = ("Pasta Fresca", 60000, ["pasta", "tomate", "albahaca"])
    LOMO_DE_BUEY = ("Lomo de Buey", 135000, ["lomo de buey", "sal", "pimienta"])
    TARTAR_DE_ATUN = ("Tartar de Atún", 98000, ["atun", "aguacate", "salsa de soya"])
    RAVIOLI_DE_TRUFA = ("Ravioli de Trufa", 115000, ["ravioli", "trufa", "queso parmesano"])

    def __init__(self, nombre, precio, ingredientes):
        self._nombre = nombre
        self._precio = precio
        self._ingredientes = ingredientes

    @staticmethod
    def obtener_todos_los_ingredientes():
        ingredientes = []
        for plato in Menu:
            ingredientes.extend(plato.get_ingredientes())
        return ingredientes

    @staticmethod
    def ingrediente_esta_duplicado(ingrediente, todos_ingredientes):
        return todos_ingredientes.count(ingrediente) > 1

    @staticmethod
    def plato_contiene_alergia(plato, alergias):
        return any(ingrediente.lower() in map(str.lower, alergias) for ingrediente in plato.get_ingredientes())

    def get_ingredientes(self):
        return self._ingredientes

    def get_precio(self):
        return self._precio

    def get_nombre(self):
        return self._nombre


class MenuCortesias(Enum):
    ENTRADA_PANES_AJO = "Entrada de Panes de Ajo"
    SOPA_TOMATE = "Sopa de Tomate"
    COCTEL_MARGARITA = "Cóctel Margarita"
    PORCION_TORTA_CHOCOLATE = "Porción de Torta de Chocolate"
    COPA_DE_HELADO = "Copa de Helado"

    def __init__(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre
