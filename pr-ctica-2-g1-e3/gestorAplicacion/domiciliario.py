from persona import Persona

class Domiciliario(Persona):
    lista_domiciliarios = []

    def __init__(self, nombre, identificacion, prom_calificaciones, total_calificaciones):
        super().__init__(nombre, identificacion)
        self._billetera = []
        self._calificaciones = []
        self._prom_calificaciones = prom_calificaciones
        self._total_calificaciones = total_calificaciones
        self._inicializar_billetera()
        Domiciliario.lista_domiciliarios.append(self)

    def _inicializar_billetera(self):
        self.agregar_billetes(50000, 4)
        self.agregar_billetes(20000, 6)
        self.agregar_billetes(10000, 11)
        self.agregar_billetes(5000, 25)
        self.agregar_billetes(2000, 60)
        self.agregar_billetes(1000, 100)

    def agregar_billetes(self, denominacion, cantidad):
        self._billetera.extend([denominacion] * cantidad)

    @staticmethod
    def inicializar_domiciliarios():
        if not Domiciliario.lista_domiciliarios:
            Domiciliario("Carlos", 123, 4, 8)
            Domiciliario("María", 456, 3, 12)
            Domiciliario("Luis", 789, 5, 3)

    def calcular_total_billetera(self):
        return sum(self._billetera)

    def entregar_cambio(self, cambio):
        billetes_entregados = []
        monto_restante = cambio

        self._billetera.sort(reverse=True)  # Ordenar de mayor a menor

        i = 0
        while i < len(self._billetera) and monto_restante > 0:
            billete = self._billetera[i]
            if billete <= monto_restante:
                billetes_entregados.append(billete)
                monto_restante -= billete
                self._billetera.pop(i)
            else:
                i += 1

        if monto_restante > 0:
            print(f"No se pudo entregar el cambio completo. Falta: {monto_restante}")

        return billetes_entregados

    def actualizar_desempeno_domiciliario(self, calificacion):
        suma_acumulada = self._prom_calificaciones * self._total_calificaciones
        self._total_calificaciones += 1
        self._prom_calificaciones = round((suma_acumulada + calificacion.get_tiempo_espera()) / self._total_calificaciones, 1)

    @staticmethod
    def get_lista_domiciliarios():
        return Domiciliario.lista_domiciliarios

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_calificaciones(self):
        return self._calificaciones

    def get_prom_calificaciones(self):
        return self._prom_calificaciones
