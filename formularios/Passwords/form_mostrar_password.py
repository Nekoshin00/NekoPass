import tkinter as tk
from tkinter import ttk
from typing_extensions import Literal
import util.util_ventana as util_ventana
from config import COLOR_MENU_LATERAL

class FormMostrarPassword(tk.Toplevel):

    def __init__(self, user, password) -> None:
        super().__init__()
        self.user = user
        self.password = password
        self.show_password = False
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Password')
        self.iconbitmap("./imagenes/neko.ico")
        self.config(background=COLOR_MENU_LATERAL)
        w, h = 400, 150
        util_ventana.centrar_ventana(self, w, h)
        self.resizable(False,False)
    
    def contruirWidget(self):
        self.lb_usuario = tk.Label(self, text="Usuario", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_usuario.grid(row=0, column=0, sticky='W')

        self.text_usuario = tk.Entry(self, font=(20), width=30)
        self.text_usuario.grid(row=0, column=1, sticky='W')

        self.lb_pass = tk.Label(self, text="Password", font=(20), padx=10, pady=10, bg=COLOR_MENU_LATERAL, fg="white")
        self.lb_pass.grid(row=1, column=0, sticky='W')

        self.text_pass = tk.Entry(self, font=(20), width=30, show="*")
        self.text_pass.grid(row=1, column=1, sticky='W')

        self.btn_toggle = tk.Button(self, text="_", width=1, command=self.toggle_password)
        self.btn_toggle.grid(row=1, column=2, padx=8)

        self.btn_copiar = tk.Button(self, text="Copiar", width=16, command=self.copiar_pass)
        self.btn_copiar.place(x=94, y=100)

        self.btn_cerrar = tk.Button(self, text="Cerrar", width=16, command=self.destroy)
        self.btn_cerrar.place(x=246, y=100)

        self.text_usuario.insert(0, f"{self.user}")
        self.text_pass.insert(0, f"{self.password}")

    def toggle_password(self):
        if self.show_password:
            self.text_pass.config(show="*")
            self.btn_toggle.config(text="_")
        else:
            self.text_pass.config(show="")
            self.btn_toggle.config(text="O")
        self.show_password = not self.show_password

    def copiar_pass(self):
        password = self.text_pass.get()
        self.clipboard_clear()
        self.clipboard_append(password)
