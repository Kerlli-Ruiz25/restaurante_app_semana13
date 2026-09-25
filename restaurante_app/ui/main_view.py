import tkinter as tk
from tkinter import messagebox


class MainView:
    """Vista principal para consultar usuarios y productos."""

    def __init__(self, root, servicio, usuario_actual, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = cerrar_sesion

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        encabezado = tk.Frame(self.frame)
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="RESTAURANTE APP - MENÚ PRINCIPAL",
            font=("Arial", 18, "bold")
        ).pack(side="left")

        tk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(side="right")

        tk.Label(
            self.frame,
            text=f"Bienvenido/a, {self.usuario_actual.nombre or self.usuario_actual.usuario}",
            font=("Arial", 11)
        ).pack(anchor="w", pady=(10, 15))

        botones = tk.Frame(self.frame)
        botones.pack(fill="x", pady=(0, 12))

        tk.Button(
            botones,
            text="Productos",
            width=18,
            command=self.mostrar_productos
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            botones,
            text="Usuarios",
            width=18,
            command=self.mostrar_usuarios
        ).pack(side="left", padx=8)

        tk.Button(
            botones,
            text="Ventas (pendiente)",
            width=18,
            command=self.ventas_pendientes
        ).pack(side="left", padx=8)

        self.contenido = tk.Text(
            self.frame,
            height=18,
            width=85,
            state="disabled",
            wrap="word"
        )
        self.contenido.pack(fill="both", expand=True)

        self.mostrar_inicio()

    def escribir_contenido(self, texto):
        self.contenido.config(state="normal")
        self.contenido.delete("1.0", tk.END)
        self.contenido.insert(tk.END, texto)
        self.contenido.config(state="disabled")

    def mostrar_inicio(self):
        total = self.servicio.consultar_cantidad_productos()
        texto = (
            "Panel principal\n\n"
            "Seleccione una opción para consultar la información cargada.\n\n"
            f"Cantidad total registrada en inventario: {total} unidades.\n\n"
            "Las opciones Ventas todavía están pendientes de desarrollo "
            "gráfico para las siguientes semanas."
        )
        self.escribir_contenido(texto)

    def mostrar_productos(self):
        productos = self.servicio.listar_productos()

        if not productos:
            self.escribir_contenido("No existen productos registrados.")
            return

        lineas = ["PRODUCTOS REGISTRADOS", ""]
        for producto in productos:
            lineas.append(
                f"ID: {producto.id} | "
                f"Producto: {producto.nombre} | "
                f"Precio: ${producto.precio:.2f} | "
                f"Cantidad: {producto.cantidad}"
            )

        self.escribir_contenido("\n".join(lineas))

    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()

        if not usuarios:
            self.escribir_contenido("No existen usuarios registrados.")
            return

        lineas = ["USUARIOS REGISTRADOS", ""]
        for usuario in usuarios:
            lineas.append(
                f"ID: {usuario.id} | "
                f"Usuario: {usuario.usuario} | "
                f"Nombre: {usuario.nombre}"
            )

        self.escribir_contenido("\n".join(lineas))

    def ventas_pendientes(self):
        messagebox.showinfo(
            "Ventas",
            "La funcionalidad de ventas queda pendiente para una etapa posterior."
        )

    def destruir(self):
        self.frame.destroy()
