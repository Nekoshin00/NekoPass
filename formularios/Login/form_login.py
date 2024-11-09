from formularios.Login.form_login_design import FormLoginDesign
from formularios.Login.form_create_user import CreateUser
from sql.funciones_login import FuncionesLogin
from tkinter import messagebox
import tkinter as tk 

class FormLogin(FormLoginDesign):
    
    def __init__(self):
        super().__init__()
        self.funciones = FuncionesLogin()

    def btn_crear_user(self):
        CreateUser()

    def validar(self):
        from formularios.form_maestro_design import FormularioMaestroDesign
        username = self.text_usuario.get()
        password = self.text_password.get()
        user = self.funciones.validar_user(username, password)

        if user:
            self.id_user = user.id_usuario
            self.usuario = user.nombre_usuario
            self.username = user.nombre_completo
            self.destroy()
            app_maestro = FormularioMaestroDesign(self.id_user, self.username, self.usuario)
            app_maestro.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrecto")
