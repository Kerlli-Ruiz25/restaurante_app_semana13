class Usuario:
    """Representa un usuario utilizado para la simulación de acceso."""

    def __init__(self, id, usuario, contrasena, nombre=""):
        self.id = id
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre

    def __str__(self):
        return self.nombre or self.usuario
