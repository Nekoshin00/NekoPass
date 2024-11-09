import tkinter as tk
from tkinter import messagebox
from typing_extensions import Literal
import util.util_ventana as util_ventana
from config import COLOR_MENU_LATERAL, FUENTE_LETRA
from sql.funciones_login import FuncionesLogin

class CreateUser(tk.Toplevel):

    def __init__(self) -> None:
        super().__init__()
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
        #Name
        self.lb_name = tk.Label(self, text="Nombre Completo", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_name.grid(row=0, column=0, sticky='W', pady=5)
        self.text_name = tk.Entry(self, font=(20), width=30)
        self.text_name.grid(row=0, column=1, sticky='W', pady=5)

        #Username
        self.lb_usuario = tk.Label(self, text="Usuario", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_usuario.grid(row=1, column=0, sticky='W', pady=0)
        self.text_usuario = tk.Entry(self, font=(20), width=30)
        self.text_usuario.grid(row=1, column=1, sticky='W',pady=0)

        #Password
        self.lb_pass = tk.Label(self, text="Password", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_pass.grid(row=2, column=0, sticky='W', pady=5)
        self.text_pass = tk.Entry(self, font=(20), width=30)
        self.text_pass.grid(row=2, column=1, sticky='W',pady=5)

        self.btn_agregar = tk.Button(self, text="Agregar", width=16)
        self.btn_agregar.config(command=self.crear_user)
        self.btn_agregar.place(x=152, y=160)

        self.btn_cerrar = tk.Button(self, text="Cerrar", width=16)
        self.btn_cerrar.config(command=self.destroy)
        self.btn_cerrar.place(x=304, y=160)

    def crear_user(self):
        nombre = self.text_name.get()
        usuario = self.text_usuario.get()
        password = self.text_pass.get()

        if not nombre:
            messagebox.showerror("Error", "Por favor ingrese su nombre")
            self.focus_set()
        elif not usuario:
            messagebox.showerror("Error", "Por favor ingrese un usuario")
            self.focus_set()
        elif not password:
            messagebox.showerror("Error", "Por favor ingrese una contraseña")
            self.focus_set()
        else:
            # Verificar si ya existe el usuario en la base de datos
            if self.funciones.existe_usuario(usuario):
                messagebox.showerror("Error", f"El usuario '{usuario}' ya existe")
            else:
                # Crear el nuevo usuario si no existe
                self.funciones.crear_user(nombre, usuario, password)
                messagebox.showinfo("Éxito", "Usuario creado correctamente")
                self.text_name.delete(0, tk.END)
                self.text_usuario.delete(0, tk.END)
                self.text_pass.delete(0, tk.END)
                self.destroy()
