import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from config import COLOR_MENU_LATERAL, FUENTE_LETRA, COLOR_CUERPO_PRINCIPAL
import util.util_ventana as util_ventana
import util.util_imagenes as util_img


class FormLoginDesign(tk.Tk):
    
    def __init__(self):                                   
        super().__init__()
        self.title('Inicio de sesion')
        self.iconbitmap("./imagenes/neko.ico")
        self.geometry('800x500')
        self.config(bg=COLOR_CUERPO_PRINCIPAL)
        self.resizable(width=0, height=0)    
        util_ventana.centrar_ventana(self, 800, 500)
        
        logo = util_img.leer_imagen("./imagenes/neko.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg=COLOR_MENU_LATERAL)
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg=COLOR_MENU_LATERAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # frame_form
        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg=COLOR_CUERPO_PRINCIPAL)
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=(FUENTE_LETRA, 30), bg=COLOR_CUERPO_PRINCIPAL, pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg=COLOR_CUERPO_PRINCIPAL)
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(FUENTE_LETRA, 14), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.text_usuario = ttk.Entry(frame_form_fill, font=(FUENTE_LETRA, 14))
        self.text_usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(FUENTE_LETRA, 14), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.text_password = ttk.Entry(frame_form_fill, font=(FUENTE_LETRA, 14))
        self.text_password.pack(fill=tk.X, padx=20, pady=10)
        self.text_password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=(FUENTE_LETRA, 15, BOLD), bg=COLOR_MENU_LATERAL, bd=0, fg="#fff", command=self.validar)
        inicio.pack(fill=tk.X, padx=20, pady=20)        
        inicio.bind("<Return>", (lambda event: self.validar()))

        btn_registrar = tk.Button(frame_form_fill, text="Crear Cuenta", font=(FUENTE_LETRA, 10, BOLD), bg=COLOR_MENU_LATERAL, bd=0, fg="#fff", command=self.btn_crear_user)
        btn_registrar.pack(fill=tk.X,padx=20)
        btn_registrar.bind("<Return>", (lambda event: self.btn_crear_user()))

        def validar(self):
            pass

        def btn_crear_user(self):
            pass
