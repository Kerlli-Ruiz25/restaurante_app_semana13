from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    """Centraliza las operaciones de usuarios y productos del restaurante."""

    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self._usuarios = []
        self._productos = []
        self.cargar_datos()

    def cargar_datos(self):
        datos_usuarios = self.archivo_servicio.cargar_usuarios()
        datos_productos = self.archivo_servicio.cargar_productos()

        self._usuarios = [
            Usuario(
                item["id"],
                item["usuario"],
                item["contrasena"],
                item.get("nombre", "")
            )
            for item in datos_usuarios
        ]

        self._productos = [
            Producto(
                item["id"],
                item["nombre"],
                item["precio"],
                item["cantidad"]
            )
            for item in datos_productos
        ]

    def validar_acceso(self, usuario, contrasena):
        usuario = usuario.strip()

        for item in self._usuarios:
            if item.usuario == usuario and item.contrasena == contrasena:
                return item

        return None

    def listar_usuarios(self):
        return list(self._usuarios)

    def listar_productos(self):
        return list(self._productos)

    def consultar_cantidad_productos(self):
        return sum(producto.cantidad for producto in self._productos)
