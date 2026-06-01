# 📂 Organizador Automático de Archivos

Proyecto desarrollado en Python para organizar automáticamente archivos dentro de una carpeta según su extensión.

## 🚀 Funcionalidades

- Detecta archivos dentro de una carpeta determinada.
- Crea automáticamente las carpetas necesarias si no existen.
- Clasifica archivos según su extensión.
- Mueve cada archivo a su carpeta correspondiente.
- Informa archivos cuya extensión no está configurada.
- Detecta carpetas no contempladas y avisa para revisión manual.

## 📁 Extensiones soportadas

| Extensión | Carpeta destino |
|------------|----------------|
| .pdf | Pdfs |
| .jpg | Images |
| .png | Images |
| .docx | Docs |
| .exe | Exe y Zip |
| .zip | Exe y Zip |
| .txt | Textos |

Las extensiones pueden ampliarse fácilmente agregando nuevas entradas al diccionario de categorías.

## 🛠 Tecnologías utilizadas

- Python 3
- pathlib
- os
- shutil

## 📋 Ejemplo

### Antes

```text
CarpetaArchivos/
├── foto.jpg
├── documento.pdf
├── notas.txt
├── instalador.exe
```

### Después

```text
CarpetaArchivos/
├── Images/
│   └── foto.jpg
│
├── Pdfs/
│   └── documento.pdf
│
├── Textos/
│   └── notas.txt
│
└── Exe y Zip/
    └── instalador.exe
```

## ⚙️ Configuración

Modificar la variable:

```python
ruta_base = pathlib.Path(r"RUTA_DE_LA_CARPETA")
```

para indicar la carpeta que se desea organizar.

También es posible personalizar las categorías editando el diccionario:

```python
dicc_car = {
    ".pdf": "Pdfs",
    ".jpg": "Images",
    ".png": "Images"
}
```

## 📚 Conceptos practicados

Durante el desarrollo de este proyecto se utilizaron los siguientes conceptos:

- Funciones
- Diccionarios
- Pathlib
- Manipulación de archivos
- Creación de directorios
- Movimiento de archivos
- Modularización de código
- Validación de datos

## 🔮 Posibles mejoras futuras

- Interfaz gráfica.
- Soporte para más extensiones.
- Lectura de configuración desde JSON.
- Organización de subcarpetas.
- Registro de acciones en un archivo de log.
- Clasificación basada en fechas.

## 👨‍💻 Sobre el proyecto

Proyecto realizado como práctica de automatización con Python para reforzar el manejo de archivos, directorios y estructuras de datos.

El objetivo fue desarrollar una herramienta capaz de organizar automáticamente una carpeta de trabajo de forma sencilla y extensible.
