import json
from pathlib import Path


class ArchivoServicio:
    """Se encarga exclusivamente de leer información desde archivos JSON."""

    def __init__(self, ruta_base=None):
        if ruta_base is None:
            ruta_base = Path(__file__).resolve().parent.parent / "datos"
        self.ruta_base = Path(ruta_base)

    def leer_json(self, nombre_archivo):
        ruta = self.ruta_base / nombre_archivo

        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        except json.JSONDecodeError as error:
            raise ValueError(f"El archivo {nombre_archivo} no contiene un JSON válido.") from error

    def cargar_productos(self):
        return self.leer_json("productos.json")

    def cargar_usuarios(self):
        return self.leer_json("usuarios.json")
