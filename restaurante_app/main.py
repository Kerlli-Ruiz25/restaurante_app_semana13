import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:
    """Controlador principal de la aplicación."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurante App - Gestión Principal")
        self.root.geometry("850x560")
        self.root.minsize(720, 480)

        archivo_servicio = ArchivoServicio()
        self.restaurante_servicio = RestauranteServicio(archivo_servicio)

        self.login_view = None
        self.main_view = None

        self.mostrar_login()

    def limpiar_vista(self):
        if self.login_view is not None:
            self.login_view.destruir()
            self.login_view = None

        if self.main_view is not None:
            self.main_view.destruir()
            self.main_view = None

    def mostrar_login(self):
        self.limpiar_vista()
        self.login_view = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self, usuario):
        self.limpiar_vista()
        self.main_view = MainView(
            self.root,
            self.restaurante_servicio,
            usuario,
            self.mostrar_login
        )

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()
