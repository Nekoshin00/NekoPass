import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from config import COLOR_CUERPO_PRINCIPAL,COLOR_BOTON_DEFAULT
#Botones

class FormPaginaDesign():

    def __init__(self, panel_principal):
        # Crear paneles: barra superior
        self.panel = panel_principal
        self.sourse = "pagina"
        self.barra_superior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)
        self.crear_botones()
        self.crear_tabla()

    def crear_botones(self):

        self.busqueda = tk.Entry(self.barra_superior,font=(20) ,border=1)
        self.busqueda.pack(side='left', padx=12, pady=10, expand=True, fill='both')
        self.busqueda.bind("<KeyRelease>", self.filtrar_lista_paginas)

        self.btn_borrar = tk.Button(self.barra_superior,text="Borrar", width=12, height=2,bg=COLOR_BOTON_DEFAULT, border=1)
        self.btn_borrar.config(command=self.eliminar_pagina)
        self.btn_borrar.pack(side='right', padx=12, pady=10, expand=False)

        self.btn_editar = tk.Button(self.barra_superior, text="Editar", width=12, height=2, bg=COLOR_BOTON_DEFAULT, border=1)
        self.btn_editar.config(command=self.editar_password)
        self.btn_editar.pack(side='right', padx=0, pady=10, expand=False)

        self.btn_agregar = tk.Button(self.barra_superior,text="Agregar", width=12, height=2, bg=COLOR_BOTON_DEFAULT, border=1)
        self.btn_agregar.config(command=self.btn_agregar_pagina)
        self.btn_agregar.pack(side='right',padx=12, pady=10, expand=False)
        
    def crear_tabla(self):
        #Tabla
        self.barra_tabla = tk.Frame(self.barra_inferior)
        self.barra_tabla.pack(side=tk.BOTTOM, fill='both', expand=True, padx=10)

        tree_scroll = tk.Scrollbar(self.barra_tabla, width=0)
        tree_scroll.pack(side='right', fill=tk.Y)

        self.tree = ttk.Treeview(self.barra_tabla, show='headings', yscrollcommand=tree_scroll.set)
        self.tree['columns'] = ('#','ID','Titulo','Cantidad')
        self.tree.column('#', width=20, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('ID', width=40, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('Titulo', anchor=tk.W, stretch=tk.YES)
        self.tree.column('Cantidad', width=80, anchor=tk.CENTER, stretch=tk.NO)

        self.tree.heading('#', text='#')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Titulo', text='Titulo')
        self.tree.heading('Cantidad', text='Cantidad')
        self.tree.pack(expand=True, fill='both')

        self.tree.bind('<Double-1>', self.on_double_click)

    def actualizar_lista():
        pass

    def on_double_click(self):
        pass

    def btn_agregar_pagina(self):
        pass

    def editar_password(self):
        pass

    def eliminar_pagina(self):
        pass

    def filtrar_lista_paginas(self):
        pass

    def limpiar_panel(self):
        for widget in self.panel.winfo_children():
            widget.destroy()

    
