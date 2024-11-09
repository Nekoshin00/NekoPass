import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
#Formularios
from formularios.Login.form_login import FormLogin
from formularios.form_info_design import FormularioInfoDesign
from formularios.Passwords.form_password import FormPasswords
from formularios.Paginas.form_pagina import FormPagina
from formularios.Dashboard.form_dashboard import FormDashboard
from formularios.Login.form_user import FormUser


class FormularioMaestroDesign(tk.Tk):

    def __init__(self, Id_user, Username, Usuario):
        super().__init__()
        self.id_user = Id_user
        self.usuario = Usuario
        self.username = Username
        self.historial = []
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (560, 136))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        self.title('NekoPass')
        self.iconbitmap("./imagenes/neko.ico")
        w, h = 1024, 600
        self.minsize(w,h)
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Main Form")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", width=4, padx=2)
        self.buttonMenuLateral.pack(side=tk.LEFT, fill='both')
        self.bind_hover_events(self.buttonMenuLateral)

        # Boton de informacion
        self.btn_user = tk.Button(self.barra_superior, text=f"Usuario: {self.username}", anchor="w", font=('FontAwesome', 10),
                                   bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", height=2, padx=5, command=self.abrir_panel_user)
        self.btn_user.pack(side='right',fill='y')
        self.bind_hover_events(self.btn_user)

        # Botón "Volver"
        self.btn_volver = tk.Button(self.barra_superior, text="Volver", anchor="w", font=('FontAwesome', 10),
                                   bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", width=5, height=2, padx=20,
                                   command=self.volver)
        self.btn_volver.pack(side='left', padx=0, fill='y')
        self.bind_hover_events(self.btn_volver)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        # Botones del menú lateral
        self.buttonDashBoard = tk.Button(self.menu_lateral)        
        self.buttonProfile = tk.Button(self.menu_lateral)        
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)        

        buttons_info = [
            ("Dashboard", "\uf03e", self.buttonDashBoard,self.abrir_dashboard),
            ("Pages", "\uf03e", self.buttonProfile,self.abrir_panel_pagina),
            ("Passwords", "\uf03e", self.buttonPicture,self.abrir_panel_password),
            ("Info", "\uf03e", self.buttonInfo,self.abrir_panel_info),
        ]

        for text, icon, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)

        #Boton Salir
        self.btn_salir = tk.Button(self.menu_lateral, text="Cerrar Sesion", anchor="w", font=('FontAwesome', 10),
                                   bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu, padx=20,
                                   command=self.cerrar_sesion)
        self.btn_salir.pack(side='bottom', fill="x")
        self.bind_hover_events(self.btn_salir)
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        pass       
  
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                      command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        if button == self.btn_volver or button == self.buttonMenuLateral or button == self.btn_user:
            button.config(bg=COLOR_BARRA_SUPERIOR, fg='white')
        else:
            button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def abrir_dashboard(self):
        self.historial.clear()
        self.historial.append(self.abrir_dashboard)
        self.limpiar_panel(self.cuerpo_principal)
        FormDashboard(self.cuerpo_principal, self.id_user)

    def abrir_panel_pagina(self):
        self.historial.clear()
        self.historial.append(self.abrir_panel_pagina)
        self.limpiar_panel(self.cuerpo_principal)
        FormPagina(self.cuerpo_principal, self.id_user)

    def abrir_panel_password(self):
        self.historial.clear()
        self.historial.append(self.abrir_panel_password)
        self.limpiar_panel(self.cuerpo_principal)
        FormPasswords(self.cuerpo_principal,None,None,self.id_user)

    def abrir_panel_info(self):           
        FormularioInfoDesign()

    def abrir_panel_user(self):
        FormUser(self, self.id_user, self.username, self.usuario)

    def volver(self):
        if self.historial:
            ultima_funcion = self.historial.pop()
            self.limpiar_panel(self.cuerpo_principal)
            ultima_funcion()
        else:
            self.abrir_dashboard()

    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def cerrar_sesion(self):
        self.destroy()
        app_login = FormLogin()
        app_login.mainloop()