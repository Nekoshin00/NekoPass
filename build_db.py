import sqlalchemy as db
import util.generic as gen
import dominio.modelos as modelos

def app_build():
    nombre_carpeta = "db"
    ruta = "./"

    gen.crear_carpeta_si_no_existe(ruta, nombre_carpeta)
    gen.generar_key()

    engine = db.create_engine('sqlite:///db/db.sqlite', echo=False, future=True)

    modelos.Base.metadata.create_all(engine)
