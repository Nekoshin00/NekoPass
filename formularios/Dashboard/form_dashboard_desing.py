import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL, FUENTE_LETRA,COLOR_MENU_LATERAL
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class FormDashboardDesign:

    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.barra_inferior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.count_pages = self.obtener_conteo_paginas()

        datos = self.obtener_datos_grafico()
        if not datos:
            return

        self.labels = list(datos.keys())
        self.sizes = list(datos.values())
        self.total = sum(self.sizes)

        

        self.generar_widgets()

    def generar_widgets(self):
        #Cantidad
        self.cantidad_passwords = tk.LabelFrame(self.barra_superior, text="Passwords", fg="white",
                                                bg=COLOR_MENU_LATERAL, height=100, width=200, border=1,
                                                font=(FUENTE_LETRA, 14))
        self.cantidad_passwords.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        self.cantidad_passwords.pack_propagate(False)
        self.lb_cantidad = tk.Label(self.cantidad_passwords, font=(FUENTE_LETRA, 20), text=self.total, fg="white",bg=COLOR_MENU_LATERAL)
        self.lb_cantidad.pack(side="left", expand=True)

        #Paginas
        self.cantidad_Paginas = tk.LabelFrame(self.barra_superior, text="Pages", fg="white",
                                                bg=COLOR_MENU_LATERAL, height=100, width=200, border=1,
                                                font=(FUENTE_LETRA, 14))
        self.cantidad_Paginas.pack(side="left", fill="both", padx=0, pady=10, expand=True)
        self.cantidad_Paginas.pack_propagate(False)
        self.lb_cantidad_paginas = tk.Label(self.cantidad_Paginas, font=(FUENTE_LETRA, 20), text=self.count_pages, fg="white",bg=COLOR_MENU_LATERAL)
        self.lb_cantidad_paginas.pack(side="left", expand=True)

        #
        self.otro = tk.LabelFrame(self.barra_superior, text="Otro", fg="white",
                                                bg=COLOR_MENU_LATERAL, height=100, width=200, border=1,
                                                font=(FUENTE_LETRA, 14))
        self.otro.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        self.otro.pack_propagate(False)

        self.grafico_pastel = tk.LabelFrame(self.barra_inferior, text="Grafico Pastel", fg="white",
                                                bg=COLOR_MENU_LATERAL, border=1,
                                                font=(FUENTE_LETRA, 10))
        self.grafico_pastel.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        self.grafico_pastel.pack_propagate(False)

        self.grafico_barra = tk.LabelFrame(self.barra_inferior, text="Grafico Barras", fg="white",
                                                bg=COLOR_MENU_LATERAL, border=1,
                                                font=(FUENTE_LETRA, 10))
        self.grafico_barra.pack(side="right", fill="both", padx=10, pady=10, expand=True)
        self.grafico_barra.pack_propagate(False)


        colors = self.crear_grafico_pastel(self.grafico_pastel, self.labels, self.sizes)
        self.crear_grafico_barra(self.grafico_barra, self.labels, self.sizes, colors)

    def obtener_datos_grafico(self):
        pass

    def obtener_conteo_paginas(self):
        pass

    def generar_colores_pastel(self, num_colores):
        colores = []
        for _ in range(num_colores):
            r = np.random.rand()
            g = np.random.rand()
            b = np.random.rand()
            colores.append(((r + 1) / 2, (g + 1) / 2, (b + 1) / 2))
        return colores

    def color_texto(self, color):
        r, g, b = color
        luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
        return 'black' if luminance > 0.5 else 'white'

    def crear_grafico_pastel(self, parent, labels, sizes):
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.patch.set_facecolor(COLOR_CUERPO_PRINCIPAL)
        ax = fig.add_subplot(111)
        ax.set_facecolor(COLOR_CUERPO_PRINCIPAL)

        percentages = [size / self.total * 100 for size in sizes]
        colors = self.generar_colores_pastel(len(labels))
        explode = [0] * len(labels)

        self.wedges, _, autotexts = ax.pie(percentages, explode=explode, labels=None, colors=colors,
                                           autopct='%1.1f%%',
                                           shadow=True, startangle=140)
        ax.axis('equal')

        for i, autotext in enumerate(autotexts):
            autotext.set_color(self.color_texto(colors[i]))

        def on_hover(event):
            found = False
            for i, wedge in enumerate(self.wedges):
                if wedge.contains_point([event.x, event.y]):
                    if hasattr(self, 'previous_index') and self.previous_index is not None and self.previous_index != i:
                        self.wedges[self.previous_index].set_alpha(1)
                        explode[self.previous_index] = 0
                        autotexts[self.previous_index].set_text(f'{percentages[self.previous_index]:.1f}%')

                    explode[i] = 0.1
                    wedge.set_alpha(0.6)
                    autotexts[i].set_text(f'{self.sizes[i]} ({self.labels[i]})')
                    self.previous_index = i
                    found = True
                    break
            if not found and hasattr(self, 'previous_index') and self.previous_index is not None:
                self.wedges[self.previous_index].set_alpha(1)
                explode[self.previous_index] = 0
                autotexts[self.previous_index].set_text(f'{percentages[self.previous_index]:.1f}%')
                self.previous_index = None

            canvas.draw()

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=True)

        canvas.mpl_connect("motion_notify_event", on_hover)

        for wedge in self.wedges:
            wedge.set_picker(True)

        self.wedges = self.wedges

        return colors

    def crear_grafico_barra(self, parent, labels, sizes, colors):
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.patch.set_facecolor(COLOR_CUERPO_PRINCIPAL)
        ax = fig.add_subplot(111)
        ax.set_facecolor(COLOR_CUERPO_PRINCIPAL)

        #colors = self.generar_colores_pastel(len(labels))
        ax.bar(labels, sizes, color=colors)

        ax.set_xticks(np.arange(len(labels)))
        ax.set_xticklabels(labels, rotation=0, ha='center', color='black', fontsize=12)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=True)