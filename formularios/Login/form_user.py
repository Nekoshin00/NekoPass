import tkinter as tk
from tkinter import messagebox
from typing_extensions import Literal
import util.util_ventana as util_ventana
from config import COLOR_MENU_LATERAL, FUENTE_LETRA
from sql.funciones_login import FuncionesLogin
from formularios.Login.form_editar_user import EditarUser

class FormUser(tk.Toplevel):

    def __init__(self, parent, Id_user, Username, Usuario) -> None:
        super().__init__()
        self.parent = parent
        self.id_user = Id_user
        self.usuario = Usuario
        self.username = Username
        self.funciones = FuncionesLogin()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Agregar')
        self.iconbitmap("./imagenes/neko.ico")
        self.config(background=COLOR_MENU_LATERAL)
        w, h = 450, 210
        util_ventana.centrar_ventana(self, w, h)
        self.resizable(False, False)
        self.grab_set()

    def contruirWidget(self):
        lb_user = tk.Label(self,text=f"Bienvenido: {self.username}", font=(FUENTE_LETRA, 20), bg=COLOR_MENU_LATERAL, fg="white")
        lb_user.pack(side="top", pady=20)
        
        self.btn_editar = tk.Button(self, text="Editar Usuario", font=(FUENTE_LETRA, 20), bg=COLOR_MENU_LATERAL, fg="white",bd=0)
        self.btn_editar.config(command=self.editar_user)
        self.btn_editar.pack(side="left", padx=10)
        self.parent.bind_hover_events(self.btn_editar)

        self.btn_eliminar = tk.Button(self, text="Borrar Usuario", font=(FUENTE_LETRA, 20), bg=COLOR_MENU_LATERAL, fg="white",bd=0)
        self.btn_eliminar.config(command=self.eliminar_user)
        self.btn_eliminar.pack(side="right", padx=10)
        self.parent.bind_hover_events(self.btn_eliminar)

    def editar_user(self):
        EditarUser(self.id_user, self.usuario, self.parent)

    def eliminar_user(self):
        try:
            respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este usuario?\n\nEliminaras todas las contraseñas que se encuentran aqui")
            if respuesta:
                self.funciones.eliminar_user(self.id_user)
                self.destroy()
                self.parent.cerrar_sesion()
        except IndexError:
            pass
        except Exception:
            pass
