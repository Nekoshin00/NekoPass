from sqlalchemy.orm import Session
from dominio.modelos import PaginaModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sql.funciones_sql import FuncionesSql

class FuncionesPagina(FuncionesSql):

    def __init__(self):
        super().__init__()

    def obtener_pagina_por_id(self, Id) -> list[PaginaModel]:
        with Session(self.engine) as session:
            try:
                pagina = session.query(PaginaModel).filter_by(id_pagina=Id).one()
                return pagina
            except NoResultFound:
                return None

    def obtener_paginas(self, Id_user) -> list[PaginaModel]:
        paginas: PaginaModel = None
        with Session(self.engine) as session:
            paginas = session.query(PaginaModel).filter_by(id_usuario=Id_user).all()
        return paginas

    def agregar_pagina(self, Id_user, nombre,) -> list[PaginaModel]:
        pagina = PaginaModel()
        pagina.nombre_pagina = nombre
        pagina.id_usuario = Id_user

        with Session(self.engine) as session:
            session.add(pagina)
            session.commit()

    def modificar_pagina(self,Nombre_Pagina, ID_Pagina):
        try:
            with Session(self.engine) as session:
                pagina = session.query(PaginaModel).filter_by(id_pagina=ID_Pagina).one()
                pagina.nombre_pagina = Nombre_Pagina
                session.commit()
                return True
        except NoResultFound:
            print(f"No se encontró ningúna pagina con ID {ID_Pagina}")
            return False
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def eliminar_pagina(self, id):
        with Session(self.engine) as session:
            pagina = session.query(PaginaModel).filter_by(id_pagina=id).first()
            if pagina:
                try:
                    session.delete(pagina)
                    session.commit()
                except IntegrityError as e:
                    session.rollback()
            else:
                pass