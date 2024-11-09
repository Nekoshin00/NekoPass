from formularios.Passwords.form_passwords_design import FormPasswordsDesign
from sql.funciones_password import FuncionesPassword
from tkinter import messagebox

from formularios.Passwords.form_mostrar_password import FormMostrarPassword
from formularios.Passwords.form_editar_password import FormEditarPassword
from formularios.Passwords.form_agregar_password import FormAgregarPassword

class FormPasswords(FormPasswordsDesign):

    def __init__(self, panel_principal, sourse, Id_pagina, Id_user):
        super().__init__(panel_principal)
        self.password_sql = FuncionesPassword()
        self.sourse = sourse
        self.id_pagina = Id_pagina
        self.id_user = Id_user

        self.actualizar_lista()

    def actualizar_lista(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)
        
        if self.sourse == "pagina":
            passwords = self.password_sql.obtener_datos_password_por_pagina(self.id_pagina)
        else:
            passwords = self.password_sql.obtener_datos_password(self.id_user)
        
        for ref, password in enumerate(passwords):
            color = ('evenrow',) if ref % 2 else ('oddrow',)

            nombre_pagina = password.pagina.nombre_pagina if password.pagina else "N/A"
            title = password.title if password.title else "N/A"
            username = password.username if password.username else "N/A"
            url = password.url if password.url else "N/A"
            notes = password.notes if password.notes else "N/A"

            self.tree.insert(parent='', index=ref, iid=ref, text='', tags = color, values=(
                ref+1, password.id_password, nombre_pagina, title, username,"**********", url, notes))
            
    def obtener_password(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][1]
            datos = self.password_sql.obtener_password(id)
            self.usuario = datos.username
            self.password = datos.password
            FormMostrarPassword(self.usuario, self.password)
        except IndexError as e:
            messagebox.showerror("Error", f"Por favor selecciona una fila")

    def abrir_btn_agregar(self):
        if self.sourse == "pagina":
            FormAgregarPassword(self, self.sourse, self.id_pagina, self.id_user)
        else:
            FormAgregarPassword(self, None, None, self.id_user)

    def editar_password(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][1]
            FormEditarPassword(self, id, self.id_pagina, self.sourse, self.id_user)
        except IndexError as e:
            messagebox.showerror("Error", f"Por favor selecciona una fila")

    def eliminar_password(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][1]
            respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar esta contraseña?")
            if respuesta:
                self.password_sql.eliminar_password(id)
                self.actualizar_lista()
            else:
                pass
        except IndexError as e:
            messagebox.showerror("Error", f"Por favor selecciona una fila")      
        
    def filtrar_lista(self, event):
        query = self.busqueda.get().lower()
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)

        if self.sourse == "pagina":
            passwords = self.password_sql.obtener_datos_password_por_pagina(self.id_pagina)
        else:
            passwords = self.password_sql.obtener_datos_password(self.id_user)

        for ref, password in enumerate(passwords):
            id_str = str(password.id_password)
            nombre_pagina_original = password.pagina.nombre_pagina if password.pagina else "N/A"
            title_original = password.title if password.title else "N/A"
            username_original = password.username if password.username else "N/A"
            url_original = password.url if password.url else "N/A"
            notes_original = password.notes if password.notes else "N/A"

            nombre_pagina = nombre_pagina_original.lower()
            title = title_original.lower()
            username = username_original.lower()
            url = url_original.lower()
            notes = notes_original.lower()

            if query in id_str or query in nombre_pagina or query in title or query in username or query in url or query in notes:
                color = ('evenrow',) if ref % 2 else ('oddrow',)
                self.tree.insert(parent='', index=ref, iid=ref, text='', tags=color, values=(
                    ref+1, password.id_password, nombre_pagina_original, title_original, username_original, "**********", url_original, notes_original))
