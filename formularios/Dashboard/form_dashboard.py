from formularios.Dashboard.form_dashboard_desing import FormDashboardDesign
from sql.funciones_pagina import FuncionesPagina
from sql.funciones_dashboard import FuncionesDashboard

class FormDashboard(FormDashboardDesign):
    
    def __init__(self, panel_principal, Id_user):
        self.dashboard_sql = FuncionesDashboard()
        self.pagina_sql = FuncionesPagina()
        self.id_user = Id_user
        super().__init__(panel_principal)

    def obtener_datos_grafico(self):
        paginas = self.pagina_sql.obtener_paginas(self.id_user)
        conteo_por_pagina = {}

        for pagina in paginas:
            conteo = self.dashboard_sql.contar_passwords_por_pagina(pagina.id_pagina)
            if conteo > 0:
                conteo_por_pagina[pagina.nombre_pagina] = conteo

        return conteo_por_pagina
    
    def obtener_conteo_paginas(self):
        conteo = self.dashboard_sql.contar_paginas_por_user(self.id_user)
        return conteo