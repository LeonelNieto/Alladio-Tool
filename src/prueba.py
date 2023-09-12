import os

ruta_carpeta_actual = os.path.dirname(os.path.abspath(__file__))
FileLocation = os.path.join(ruta_carpeta_actual, "DefaultJson\\erd-definitions.json")

print(FileLocation)