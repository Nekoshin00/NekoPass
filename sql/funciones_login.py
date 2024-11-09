from sqlalchemy.orm import Session
from dominio.modelos import UsuarioModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt

from sql.funciones_sql import FuncionesSql

class FuncionesLogin(FuncionesSql):

    def __init__(self):
        super().__init__()

    def crear_user(self, Nombre, Usuario, Password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(Password.encode('utf-8'), salt)
        
        Users = UsuarioModel()
        Users.nombre_completo = Nombre
        Users.nombre_usuario = Usuario
        Users.password = hashed_password

        with Session(self.engine) as session:
            session.add(Users)
            session.commit()

    def existe_usuario(self, Usuario):
        with Session(self.engine) as session:
            user = session.query(UsuarioModel).filter_by(nombre_usuario=Usuario).first()
            return user is not None
        
    def obtener_password_user(self, id_user):
        with Session(self.engine) as session:
            user = session.query(UsuarioModel).filter_by(id_usuario=id_user).first()
            return user
        
    def modificar_user(self, id_user, Nombre, Usuario, Password, Old_Password):
        try:
            with Session(self.engine) as session:
                user = session.query(UsuarioModel).filter_by(id_usuario=id_user).one()
                
                if Password == Old_Password:
                    user.password = Old_Password
                else:
                    user.password = Password
                
                user.nombre_completo = Nombre
                user.nombre_usuario = Usuario
                
                session.commit()
                return True
        except NoResultFound:
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def eliminar_user(self, id):
        with Session(self.engine) as session:
            user = session.query(UsuarioModel).filter_by(id_usuario=id).first()
            if user:
                try:
                    session.delete(user)
                    session.commit()
                except IntegrityError as e:
                    session.rollback()
            else:
                pass

    def validar_user(self, Usuario, Password):     
        with Session(self.engine) as session:    
            user = session.query(UsuarioModel).filter_by(nombre_usuario=Usuario).first()
            if user is None:
                return False
            if bcrypt.checkpw(Password.encode('utf-8'), user.password):
                return user
            else:
                return False