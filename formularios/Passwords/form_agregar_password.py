import tkinter as tk
from tkinter import ttk, messagebox
from typing_extensions import Literal
import util.util_ventana as util_ventana
import util.util_genpass as genpass
from config import COLOR_MENU_LATERAL
from sql.funciones_password import FuncionesPassword
from sql.funciones_pagina import FuncionesPagina

class FormAgregarPassword(tk.Toplevel):

    def __init__(self, parent, Sourse, Id_pagina, Id_user) -> None:
        super().__init__()
        self.parent = parent
        self.sourse = Sourse
        self.id_pagina = Id_pagina
        self.id_user = Id_user
        self.password_sql = FuncionesPassword()
        self.pagina_sql = FuncionesPagina()
        self.show_password = False
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Agregar')
        self.iconbitmap("./imagenes/neko.ico")
        self.config(background=COLOR_MENU_LATERAL)
        w, h = 400, 350
        util_ventana.centrar_ventana(self, w, h)
        self.resizable(False, False)
        self.grab_set()

    def contruirWidget(self):
        #Pagina
        self.lb_pagina = tk.Label(self, text="Pagina", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_pagina.grid(row=0, column=0, sticky='W', pady=5)
        self.cbx_pagina = ttk.Combobox(self, width=28, font=(20), state="readonly")
        self.cbx_pagina.grid(row=0, column=1, sticky='W', pady=5)

        #titulo
        self.lb_titulo = tk.Label(self, text="Titulo", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_titulo.grid(row=1, column=0, sticky='W')
        self.text_titulo = tk.Entry(self, font=(20), width=30)
        self.text_titulo.grid(row=1, column=1, sticky='W')

        #Username
        self.lb_usuario = tk.Label(self, text="Usuario", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_usuario.grid(row=2, column=0, sticky='W', pady=5)
        self.text_usuario = tk.Entry(self, font=(20), width=30)
        self.text_usuario.grid(row=2, column=1, sticky='W',pady=5)

        #Password
        self.lb_pass = tk.Label(self, text="Password", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_pass.grid(row=3, column=0, sticky='W')
        self.text_pass = tk.Entry(self, show="*", font=(20), width=30)
        self.text_pass.grid(row=3, column=1, sticky='W')

        self.btn_toggle = tk.Button(self, text="_", width=1, command=self.toggle_password)
        self.btn_toggle.grid(row=3, column=2, padx=8)

        #URL
        self.lb_url = tk.Label(self, text="URL", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_url.grid(row=4, column=0, sticky='W', pady=5)
        self.text_url = tk.Entry(self, font=(20), width=30)
        self.text_url.grid(row=4, column=1, sticky='W',pady=5)

        #Notes
        self.lb_notes = tk.Label(self, text="Notas", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_notes.grid(row=5, column=0, sticky='W')
        self.text_notes = tk.Entry(self, font=(20), width=30)
        self.text_notes.grid(row=5, column=1, sticky='W')

        #Botones
        self.btn_agregar = tk.Button(self, text="Agregar", width=10)
        self.btn_agregar.config(command=self.agregar_password)
        self.btn_agregar.place(x=94, y=300)

        self.btn_agregar = tk.Button(self, text="Generar", width=10)
        self.btn_agregar.config(command=self.generar_password)
        self.btn_agregar.place(x=190, y=300)

        self.btn_cerrar = tk.Button(self, text="Cerrar", width=10)
        self.btn_cerrar.config(command=self.destroy)
        self.btn_cerrar.place(x=288, y=300)

        self.obtener_datos()
    
    def obtener_datos(self):
        if self.sourse == "pagina":
            pagina = self.pagina_sql.obtener_pagina_por_id(self.id_pagina)
            if pagina:
                datos_combobox = [(pagina.id_pagina, pagina.nombre_pagina)]
                self.pagina_dict = {pagina.nombre_pagina: pagina.id_pagina}

                opciones_combobox = [pagina.nombre_pagina]
                self.cbx_pagina['values'] = opciones_combobox

                self.cbx_pagina.set(pagina.nombre_pagina)
            else:
                self.cbx_pagina['values'] = ["No se encontró la página"]
                self.cbx_pagina.set("No se encontró la página")
        else:
            paginas = self.pagina_sql.obtener_paginas(self.id_user)
            datos_combobox = [(pagina.id_pagina, pagina.nombre_pagina) for pagina in paginas]
            self.pagina_dict = {nombre_pagina: id_pagina for id_pagina, nombre_pagina in datos_combobox}

            opciones_combobox = ["Seleccione..."] + [nombre_pagina for _, nombre_pagina in datos_combobox]
            self.cbx_pagina['values'] = opciones_combobox

            self.cbx_pagina.set("Seleccione...")

    def toggle_password(self):
        if self.show_password:
            self.text_pass.config(show="*")
            self.btn_toggle.config(text="_")
        else:
            self.text_pass.config(show="")
            self.btn_toggle.config(text="O")
        self.show_password = not self.show_password

    def generar_password(self):
        self.text_pass.delete(0, 'end')
        self.text_pass.insert(0,genpass.generar_password())

    def agregar_password(self):
        titulo = self.text_titulo.get()
        username = self.text_usuario.get()
        password = self.text_pass.get()
        url = self.text_url.get()
        notes = self.text_notes.get()

        pagina_seleccionada = self.cbx_pagina.get()
        pagina_index = self.pagina_dict.get(pagina_seleccionada, None)

        if pagina_seleccionada == "Seleccione...":
            messagebox.showerror("Error", "Por favor Seleccione una Pagina")
            self.focus_set()
        elif not titulo:
            messagebox.showerror("Error", "Por favor Ingrese un Titulo")
            self.focus_set()
        elif not username:
            messagebox.showerror("Error", "Por favor Ingrese un Usuario")
            self.focus_set()
        elif not password:
            messagebox.showerror("Error", "Por favor Ingrese una Contraseña")
            self.focus_set()
        else:
            self.password_sql.agregar_password(self.id_user, pagina_index, titulo, username, password, url, notes)
            self.parent.actualizar_lista()
            self.destroy()
