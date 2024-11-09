import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelos import PasswordModel, PaginaModel
from sql.funciones_sql import FuncionesSql

class FuncionesDashboard(FuncionesSql):

    def __init__(self):
        super().__init__()

    def contar_passwords_por_pagina(self, id_pagina: int) -> int:
        with Session(self.engine) as session:
            count = session.query(db.func.count(PasswordModel.id_password)).filter_by(id_pagina=id_pagina).scalar()
        return count

    def contar_paginas_por_user(self, id_user):
        with Session(self.engine) as session:
            count = session.query(db.func.count(PaginaModel.id_usuario)).filter_by(id_usuario=id_user).scalar()
        return count