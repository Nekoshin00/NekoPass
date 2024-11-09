from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.orm import declarative_base, relationship, Session, joinedload
from sqlalchemy.exc import IntegrityError, NoResultFound
from cryptography.fernet import Fernet
import os

Base = declarative_base()

class UsuarioModel(Base):
    __tablename__ = "Usuarios"
    id_usuario = Column("ID_Usuario", Integer, primary_key=True, autoincrement=True)
    nombre_completo = Column("Nombre_Completo", String)
    nombre_usuario = Column("Nombre_Usuario", String)
    password = Column("Password", String)

    passwords = relationship("PasswordModel", back_populates="usuario", cascade="all, delete-orphan")
    paginas = relationship("PaginaModel", back_populates="usuario", cascade="all, delete-orphan")


class PaginaModel(Base):
    __tablename__ = "Paginas"
    id_pagina = Column("ID_Pagina", Integer, primary_key=True, autoincrement=True)
    nombre_pagina = Column("Nombre_Pagina", String)
    id_usuario = Column("ID_Usuario", Integer, ForeignKey('Usuarios.ID_Usuario', ondelete="CASCADE"))

    passwords = relationship("PasswordModel", back_populates="pagina", cascade="all, delete-orphan")
    usuario = relationship("UsuarioModel", back_populates="paginas")


class PasswordModel(Base):
    __tablename__ = "Passwords"
    id_password = Column("ID_Password", Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("ID_Usuario", Integer, ForeignKey('Usuarios.ID_Usuario'))
    id_pagina = Column("ID_Pagina", Integer, ForeignKey('Paginas.ID_Pagina', ondelete="CASCADE"))
    title = Column("Title", String)
    username = Column("Username", String)
    password = Column("Password", String)
    url = Column("URL", String)
    notes = Column("Notes", String)

    usuario = relationship("UsuarioModel", back_populates="passwords")
    pagina = relationship("PaginaModel", back_populates="passwords")
