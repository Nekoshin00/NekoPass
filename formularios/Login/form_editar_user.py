import tkinter as tk
from tkinter import messagebox
from typing_extensions import Literal
import util.util_ventana as util_ventana
from config import COLOR_MENU_LATERAL, FUENTE_LETRA
from sql.funciones_login import FuncionesLogin
import bcrypt

class EditarUser(tk.Toplevel):

    def __init__(self, Id_user, Usuario, parent) -> None:
        super().__init__()
        self.funciones = FuncionesLogin()
        self.parent = parent
        self.id_user = Id_user
        self.usuario = Usuario
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Editar')
        self.iconbitmap("./imagenes/neko.ico")
        self.config(background=COLOR_MENU_LATERAL)
        w, h = 450, 240
        util_ventana.centrar_ventana(self, w, h)
        self.resizable(False, False)
        self.grab_set()

    def contruirWidget(self):
        # Nombre
        self.lb_name = tk.Label(self, text="Nombre Completo", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_name.grid(row=0, column=0, sticky='W', pady=5)
        self.text_name = tk.Entry(self, font=(20), width=30)
        self.text_name.grid(row=0, column=1, sticky='W', pady=5)

        # Usuario
        self.lb_usuario = tk.Label(self, text="Usuario", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_usuario.grid(row=1, column=0, sticky='W', pady=0)
        self.text_usuario = tk.Entry(self, font=(20), width=30)
        self.text_usuario.grid(row=1, column=1, sticky='W', pady=0)

        # Contraseña actual
        self.lb_actual_pass = tk.Label(self, text="Contraseña Actual", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_actual_pass.grid(row=2, column=0, sticky='W', pady=5)
        self.text_actual_pass = tk.Entry(self, font=(20), width=30, show="*")
        self.text_actual_pass.grid(row=2, column=1, sticky='W', pady=5)

        # Nueva contraseña (si la va a cambiar)
        self.lb_pass = tk.Label(self, text="Nueva Contraseña", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_pass.grid(row=3, column=0, sticky='W', pady=5)
        self.text_pass = tk.Entry(self, font=(20), width=30, show="*")
        self.text_pass.grid(row=3, column=1, sticky='W', pady=5)

        # Botones
        self.btn_agregar = tk.Button(self, text="Guardar", width=16)
        self.btn_agregar.config(command=self.modificar_user)
        self.btn_agregar.place(x=152, y=200)

        self.btn_cerrar = tk.Button(self, text="Cerrar", width=16)
        self.btn_cerrar.config(command=self.destroy)
        self.btn_cerrar.place(x=306, y=200)

        self.obtener_datos()

    def obtener_datos(self):
        user = self.funciones.obtener_password_user(self.id_user)
        self.text_name.insert(0, user.nombre_completo)
        self.text_usuario.insert(0, user.nombre_usuario)
        self.text_pass.delete(0, 'end')

    def modificar_user(self):
        nombre = self.text_name.get()
        usuario = self.text_usuario.get()
        actual_password = self.text_actual_pass.get()
        new_password = self.text_pass.get()
        
        password_user = self.funciones.obtener_password_user(self.id_user)
        old_password = password_user.password

        if not nombre:
            messagebox.showerror("Error", "Por favor ingrese su nombre")
            self.focus_set()
        elif not usuario:
            messagebox.showerror("Error", "Por favor ingrese un usuario")
            self.focus_set()
        elif not actual_password:
            messagebox.showerror("Error", "Por favor ingrese su contraseña actual")
            self.focus_set()
        else:
            if not bcrypt.checkpw(actual_password.encode('utf-8'), old_password):
                messagebox.showerror("Error", "La contraseña actual es incorrecta")
                self.focus_set()
            else:
                if usuario == self.usuario:
                    if new_password:
                        new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                    else:
                        new_password_hash = old_password

                    self.funciones.modificar_user(self.id_user, nombre, usuario, new_password_hash, old_password)
                    messagebox.showinfo("Éxito", "Usuario editado correctamente")
                    self.destroy()
                    self.parent.cerrar_sesion()             
                                    
                    
                else:
                    if self.funciones.existe_usuario(usuario):
                        messagebox.showerror("Error", f"El usuario '{usuario}' ya existe")
                    else:
                        if new_password:
                            new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                        else:
                            new_password_hash = old_password

                        self.funciones.modificar_user(self.id_user, nombre, usuario, new_password_hash, old_password)
                        messagebox.showinfo("Éxito", "Usuario editado correctamente")   
                        self.destroy()
                        self.parent.cerrar_sesion()
