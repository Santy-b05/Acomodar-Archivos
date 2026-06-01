import os
from shutil import move
import pathlib

ruta_base = pathlib.Path(r"Ingresar Ruta\CarpetaArchivos") # Ruta a la carpeta que se busca acomodar, el nombre de la carpeta se puede modificar
dicc_car = {".pdf": "Pdfs", ".jpg": "Images", ".png": "Images", ".docx": "Docs", ".exe": "Exe y Zip", ".zip": "Exe y Zip", ".txt": "Textos"} # Diccionario con extensiones, si se desea otra solo agregar
 
def crear_y_mover_archivos(ruta, archivo, dicc): # En caso de no existir la carpeta la crea y mueve el archivo
    exten = archivo.suffix
    carpeta = dicc.get(exten)
    if carpeta != None:
        os.makedirs(ruta / carpeta, exist_ok=True)
        move(archivo, ruta / carpeta / archivo.name)
    else:
        print(f"El archivo {archivo.stem} no se encuentra en el diccionario, no se puede ordenar")

for ruta_archivo in ruta_base.iterdir(): # Revisa cada archivo en la ruta
        if ruta_archivo.is_file(): # Revisa si es archivo o carpeta
            crear_y_mover_archivos(ruta_base, ruta_archivo, dicc_car)
        elif ruta_archivo.is_dir() and ruta_archivo.stem not in dicc_car.values():
            print(f"El archivo {ruta_archivo.name} es una carpeta, revisarla manualmente o mover archivos interiores")
print("Archivos acomodados con éxito")
