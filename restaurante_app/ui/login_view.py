import tkinter as tk
from tkinter import messagebox


class LoginView:
    """Vista gráfica para el acceso simulado a la aplicación."""

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.frame = tk.Frame(root, padx=35, pady=35)
        self.frame.pack(expand=True)

        tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        ).pack(pady=(0, 8))

        tk.Label(
            self.frame,
            text="Inicio de sesión"
        ).pack(pady=(0, 20))

        tk.Label(self.frame, text="Usuario").pack(anchor="w")
        self.usuario_entry = tk.Entry(self.frame, width=35)
        self.usuario_entry.pack(pady=(3, 12))

        tk.Label(self.frame, text="Contraseña").pack(anchor="w")
        self.contrasena_entry = tk.Entry(self.frame, width=35, show="*")
        self.contrasena_entry.pack(pady=(3, 18))

        self.mensaje = tk.Label(
            self.frame,
            text="Ingrese sus credenciales para continuar.",
            fg="gray"
        )
        self.mensaje.pack(pady=(0, 12))

        tk.Button(
            self.frame,
            text="Ingresar",
            width=20,
            command=self.ingresar
        ).pack()

        tk.Label(
            self.frame,
            text="Acceso de prueba: admin / 1234",
            fg="gray"
        ).pack(pady=(18, 0))

        self.usuario_entry.focus_set()

    def ingresar(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get()

        if not usuario or not contrasena:
            self.mensaje.config(
                text="Debe completar usuario y contraseña.",
                fg="red"
            )
            return

        usuario_validado = self.servicio.validar_acceso(usuario, contrasena)

        if usuario_validado is None:
            self.mensaje.config(
                text="Usuario o contraseña incorrectos.",
                fg="red"
            )
            self.contrasena_entry.delete(0, tk.END)
            return

        self.mensaje.config(
            text="Acceso correcto.",
            fg="green"
        )
        self.mostrar_principal(usuario_validado)

    def limpiar(self):
        self.usuario_entry.delete(0, tk.END)
        self.contrasena_entry.delete(0, tk.END)
        self.mensaje.config(
            text="Ingrese sus credenciales para continuar.",
            fg="gray"
        )
        self.usuario_entry.focus_set()

    def destruir(self):
        self.frame.destroy()
