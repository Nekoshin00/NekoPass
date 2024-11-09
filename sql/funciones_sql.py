import os
import sqlalchemy as db
import logging
from cryptography.fernet import Fernet

class FuncionesSql():

    def __init__(self):

        logging.basicConfig()
        logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

        self.engine = db.create_engine('sqlite:///db/db.sqlite', echo=False, future=True)
        key_path = "./secret.key"
        if not os.path.isfile(key_path):
            raise FileNotFoundError(f"No se encontró el archivo de clave en {key_path}")
        try:
            with open(key_path, "rb") as key_file:
                self.key = key_file.read()
            self.cipher_suite = Fernet(self.key)
        except Exception as e:
            raise RuntimeError(f"Error al leer el archivo de clave: {e}")
