import tkinter as tk
from tkinter import ttk
from typing_extensions import Literal
import util.util_ventana as util_ventana
from config import COLOR_MENU_LATERAL
from sql.funciones_pagina import FuncionesPagina

class FormAgregarPagina(tk.Toplevel):

    def __init__(self, parent, Id_user) -> None:
        super().__init__()
        self.parent = parent
        self.id_user = Id_user
        self.pagina_sql = FuncionesPagina()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Agregar')
        self.iconbitmap("./imagenes/neko.ico")
        self.config(background=COLOR_MENU_LATERAL)
        w, h = 400, 100
        util_ventana.centrar_ventana(self, w, h)
        self.resizable(False, False)

    def contruirWidget(self):
        self.lb_pagina = tk.Label(self, text="Nombre", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_pagina.grid(row=0, column=0, sticky='W')

        self.text_pagina = tk.Entry(self, font=(20), width=30)
        self.text_pagina.grid(row=0, column=1, sticky='W')

        self.btn_agregar = tk.Button(self, text="Agregar", width=16)
        self.btn_agregar.config(command=self.agregar_pagina)
        self.btn_agregar.place(x=80, y=50)

        self.btn_cerrar = tk.Button(self, text="Cerrar", width=16)
        self.btn_cerrar.config(command=self.destroy)
        self.btn_cerrar.place(x=232, y=50)

    def agregar_pagina(self):
        pagina = self.text_pagina.get()
        self.pagina_sql.agregar_pagina(self.id_user, pagina)
        self.parent.actualizar_lista()
        self.destroy()
