from formularios.Paginas.form_pagina_design import FormPaginaDesign
from formularios.Paginas.form_editar_pagina import FormEditarPagina
from formularios.Paginas.form_agregar_pagina import FormAgregarPagina
from formularios.Passwords.form_password import FormPasswords
from sql.funciones_pagina import FuncionesPagina
from sql.funciones_dashboard import FuncionesDashboard
from tkinter import messagebox

class FormPagina(FormPaginaDesign):

    def __init__(self, panel_principal, Id_user):
        super().__init__(panel_principal)
        self.pagina_sql = FuncionesPagina()
        self.dashboard_sql = FuncionesDashboard()
        self.id_user = Id_user
        self.actualizar_lista()

    def actualizar_lista(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)

        paginas = self.pagina_sql.obtener_paginas(self.id_user)
        for ref, pagina in enumerate(paginas):
            color = ('evenrow',) if ref % 2 else ('oddrow',)
            cantidad_passwords = self.dashboard_sql.contar_passwords_por_pagina(pagina.id_pagina)
            
            self.tree.insert(parent='', index=ref, iid=ref, text='', tags=color, 
                            values=(ref + 1, pagina.id_pagina, pagina.nombre_pagina, cantidad_passwords))
            
    def btn_agregar_pagina(self):
        FormAgregarPagina(self, self.id_user)

    def editar_password(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][1]
            FormEditarPagina(self, id)
        except IndexError as e:
            messagebox.showerror("Error", f"Por favor selecciona una fila")
            
    def eliminar_pagina(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][1]
            respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar esta pagina?\n\nEliminaras todas las contraseñas que se encuentran aqui")
            if respuesta:
                self.pagina_sql.eliminar_pagina(id)
                self.actualizar_lista()
            else:
                pass
        except IndexError as e:
            messagebox.showerror("Error", "Por favor selecciona una fila")    

    def filtrar_lista_paginas(self, event):
        query = self.busqueda.get().lower()
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)

        paginas = self.pagina_sql.obtener_paginas(self.id_user)
        for ref, pagina in enumerate(paginas):
            
            id_str = str(pagina.id_pagina)
            nombre_pagina = pagina.nombre_pagina.lower()

            if query in id_str or query in nombre_pagina:
                color = ('evenrow',) if ref % 2 else ('oddrow',)
                self.tree.insert(parent='', index=ref, iid=ref, text='', tags=color, values=(
                    ref+1, pagina.id_pagina, pagina.nombre_pagina))
                
    def on_double_click(self, event):
        try:
            Id = self.tree.item(self.tree.selection())["values"][1]
            self.limpiar_panel()
            FormPasswords(self.panel, self.sourse, Id, self.id_user)
        except IndexError as e:
            messagebox.showerror("Error", f"Por favor selecciona una fila")