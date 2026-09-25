class Producto:
    """Representa un producto registrado en el restaurante."""

    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.cantidad}"
