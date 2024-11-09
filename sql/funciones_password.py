from sqlalchemy.orm import Session, joinedload
from dominio.modelos import PasswordModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sql.funciones_sql import FuncionesSql

class FuncionesPassword(FuncionesSql):

    def __init__(self):
        super().__init__()

    def obtener_datos_password_por_pagina(self, Id) -> list[PasswordModel]:
        with Session(self.engine) as session:
            passwords = session.query(PasswordModel).options(joinedload(PasswordModel.usuario), joinedload(PasswordModel.pagina)).filter_by(id_pagina=Id).all()
            for password in passwords:
                password.title = self.cipher_suite.decrypt(password.title.encode()).decode()
                password.username = self.cipher_suite.decrypt(password.username.encode()).decode()
                password.password = self.cipher_suite.decrypt(password.password.encode()).decode()
                password.url = self.cipher_suite.decrypt(password.url.encode()).decode()
                password.notes = self.cipher_suite.decrypt(password.notes.encode()).decode()
        return passwords

    def obtener_datos_password(self, Id_user) -> list[PasswordModel]:
        with Session(self.engine) as session:
            passwords = session.query(PasswordModel).options(joinedload(PasswordModel.usuario), joinedload(PasswordModel.pagina)).filter_by(id_usuario=Id_user).all()
            for password in passwords:
                password.title = self.cipher_suite.decrypt(password.title.encode()).decode()
                password.username = self.cipher_suite.decrypt(password.username.encode()).decode()
                password.password = self.cipher_suite.decrypt(password.password.encode()).decode()
                password.url = self.cipher_suite.decrypt(password.url.encode()).decode()
                password.notes = self.cipher_suite.decrypt(password.notes.encode()).decode()
        return passwords

    def agregar_password(self, ID_Usuario, ID_Pagina, Title, Username, Password, URL, Notes):

        encrypted_title = self.cipher_suite.encrypt(Title.encode()).decode()
        encrypted_username = self.cipher_suite.encrypt(Username.encode()).decode()
        encrypted_password = self.cipher_suite.encrypt(Password.encode()).decode()
        encrypted_url = self.cipher_suite.encrypt(URL.encode()).decode()
        encrypted_notes = self.cipher_suite.encrypt(Notes.encode()).decode()

        password = PasswordModel()

        password.id_usuario = ID_Usuario
        password.id_pagina = ID_Pagina
        password.title = encrypted_title
        password.username = encrypted_username
        password.password = encrypted_password
        password.url = encrypted_url
        password.notes = encrypted_notes

        with Session(self.engine) as session:
            session.add(password)
            session.commit()

    def modificar_pass(self,ID_Usuario, ID_Pagina, Title, Username, Password, URL, Notes, ID_Password):
        try:
            encrypted_title = self.cipher_suite.encrypt(Title.encode()).decode()
            encrypted_username = self.cipher_suite.encrypt(Username.encode()).decode()
            encrypted_password = self.cipher_suite.encrypt(Password.encode()).decode()
            encrypted_url = self.cipher_suite.encrypt(URL.encode()).decode()
            encrypted_notes = self.cipher_suite.encrypt(Notes.encode()).decode()

            with Session(self.engine) as session:
                password = session.query(PasswordModel).filter_by(id_password=ID_Password).one()

                password.id_usuario = ID_Usuario
                password.id_pagina = ID_Pagina
                password.title = encrypted_title
                password.username = encrypted_username
                password.password = encrypted_password
                password.url = encrypted_url
                password.notes = encrypted_notes
                        
                session.commit()
                return True
        except NoResultFound:
            return False
        except Exception as e:
            return False

    def eliminar_password(self, id):
        with Session(self.engine) as session:
            password = session.query(PasswordModel).filter_by(id_password=id).first()
            if password:
                try:
                    session.delete(password)
                    session.commit()
                except IntegrityError as e:
                    session.rollback()
            else:
                pass

    def obtener_password(self, id) -> PasswordModel:
        with Session(self.engine) as session:
            try:
                password = session.query(PasswordModel).options(joinedload(PasswordModel.pagina)).filter_by(id_password=id).one()

                password.title = self.cipher_suite.decrypt(password.title.encode()).decode()
                password.username = self.cipher_suite.decrypt(password.username.encode()).decode()
                password.password = self.cipher_suite.decrypt(password.password.encode()).decode()
                password.url = self.cipher_suite.decrypt(password.url.encode()).decode()
                password.notes = self.cipher_suite.decrypt(password.notes.encode()).decode()

                return password
            except NoResultFound:
                return None