import os
from cryptography.fernet import Fernet


def crear_carpeta_si_no_existe(ruta, nombre_carpeta):

    ruta_completa = os.path.join(ruta, nombre_carpeta)
    
    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
        return True, f"Se ha creado la carpeta '{nombre_carpeta}' en '{ruta}'"
    else:
        return False, f"La carpeta '{nombre_carpeta}' ya existe en '{ruta}'"

def generar_key():
    if not os.path.exists("secret.key"):
        clave = Fernet.generate_key()

        with open("secret.key", "wb") as archivo_clave:
            archivo_clave.write(clave)
        return True, "Se ha generado una nueva clave y guardado en 'secret.key'."
    else:
        return False, "La clave ya existe en 'secret.key'."