class PedidoItem:
    _pedido_items = []  # Lista estática para almacenar los items del pedido

    def __init__(self, producto: str, cantidad: int):
        self._producto = producto
        self._cantidad = cantidad
        PedidoItem._pedido_items.append(self)

    def get_producto(self):
        return self._producto

    def set_producto(self, producto: str):
        self._producto = producto

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad: int):
        self._cantidad = cantidad

    def __str__(self):
        return f"{self._producto} x {self._cantidad}"

    @staticmethod
    def get_pedido_items():
        return PedidoItem._pedido_items
