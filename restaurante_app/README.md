# Restaurante App - Semana 13

## Asignatura
Programación Orientada a Objetos

## Tema
Conceptos fundamentales de interfaces gráficas de usuario.

## Propósito

Esta versión de `restaurante_app` adapta la estructura del proyecto docente de la Semana 13 para iniciar la transición de una aplicación de consola a una aplicación con interfaz gráfica utilizando Tkinter.

En esta etapa se trabajan únicamente los modelos `Producto` y `Usuario`, los servicios de lectura y gestión de información, y las vistas `LoginView` y `MainView`.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Responsabilidades

- `datos/`: contiene la información local en formato JSON.
- `modelos/`: representa las entidades Producto y Usuario.
- `servicios/`: lee los JSON y concentra las operaciones de usuarios y productos.
- `ui/`: contiene las vistas gráficas construidas con Tkinter.
- `main.py`: crea una única ventana principal, prepara las dependencias y controla el cambio entre LoginView y MainView.

## Flujo de la aplicación

```text
Inicio
  ↓
main.py
  ↓
LoginView
  ↓
Usuario y contraseña
  ↓
RestauranteServicio valida el acceso
  ↓
MainView
  ↓
Productos / Usuarios / Ventas pendiente
  ↓
Cerrar sesión
  ↓
LoginView
```

## Credenciales de prueba

- Usuario: `admin`
- Contraseña: `1234`

También existe:

- Usuario: `kerli`
- Contraseña: `1234`

## Ejecución

1. Tener Python 3 instalado.
2. Abrir una terminal dentro de la carpeta `restaurante_app`.
3. Ejecutar:

```bash
python main.py
```

En Windows también puede utilizarse:

```bash
py main.py
```

No se necesitan librerías externas, porque la interfaz utiliza `tkinter`, incluida normalmente con Python para Windows.

## Comprobaciones realizadas

La aplicación está preparada para:

- Mostrar primero el inicio de sesión.
- Validar campos vacíos.
- Validar usuario y contraseña mediante `RestauranteServicio`.
- Mostrar la interfaz principal después del acceso correcto.
- Consultar productos desde `RestauranteServicio`.
- Consultar usuarios desde `RestauranteServicio`.
- Mantener la opción Ventas como funcionalidad pendiente.
- Cerrar sesión y regresar al login dentro de la misma ventana.
- Utilizar una sola instancia de `Tk()` y un solo `mainloop()`.

## Alcance de la Semana 13

No se implementan todavía ventas completas, bases de datos, autenticación real, formularios avanzados ni nuevas entidades. Estas funcionalidades pueden incorporarse posteriormente conforme avance la unidad.
