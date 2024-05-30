from tkinter import * 
from tkinter import ttk
import tkinter as tk
import socket

import phpFuncs
import alumnos_funciones
import sistemas_funciones
import practicas_funciones

class lab_app:
    def __init__(self, title="Simple Window", width=300, height=200):
        self.root = Tk()
        self.root.title(title)
        self.root.configure(bg='#31297B')  # Establece el color de fondo de la ventana
        # Make the window fullscreen
        self.root.attributes('-fullscreen', True)

        # Definición de estilos y colores
        self.fuente_Titulo = ('Arial', 20, 'bold')
        self.fuente_Subtitulo = ('Arial', 11, 'bold')
        self.fuente_Entry = ('Arial', 8)
        self.color_verde = "#367B2C"
        self.color_amarillo = "#FFDE00"
        self.color_gris = "#404040"
        self.color_blanco = "#FFFFFF"
        self.color_morado = "#7B2973"
        self.color_azul = "#31297B"

        self.selected_option = None 
        
        # Bind the Escape key to exit fullscreen mode
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.geometry(f"{width}x{height}")

        self.ip_conn = socket.gethostbyname(socket.gethostname())
        print(self.ip_conn)

        
        for i in range(18):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(12):
            self.root.grid_columnconfigure(i, weight=1)

        self.create_widgets()

    def cleanWindow(self):
        # Función para limpiar la ventana de Tkinter
        widgets = self.root.winfo_children()  # Obtiene una lista de todos los widgets en la ventana
        # Elimina o destruye cada widget
        for widget in widgets:
            widget.destroy()

    def create_widgets(self):
        self.cleanWindow()
        self.alumno_button = tk.Button(self.root, text="Alumnos",fg = self.color_blanco,bg= self.color_gris,font=self.fuente_Titulo,command=self.viz_alumno,width=15, height=3, justify='center', wraplength=200)
        self.alumno_button.grid(row=9,column=3,sticky = "nswe")
        self.sistema_button = tk.Button(self.root, text="Sistemas",fg = self.color_blanco,bg= self.color_gris,font=self.fuente_Titulo,command=self.viz_sistema,width=15, height=3, justify='center', wraplength=200)
        self.sistema_button.grid(row=9,column=6,sticky = "nswe")
        self.lab_button = tk.Button(self.root, text="Laboratorios",fg =self.color_blanco, bg= self.color_gris,font=self.fuente_Titulo,command=self.laboratorio_opciones,width=15, height=3, justify='center', wraplength=200)
        self.lab_button.grid(row=9,column=9,sticky = "nswe")

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

    def actualizar_treemap(self,lista_datos):
        for item in self.treemap.get_children():
            self.treemap.delete(item)
        for dato in lista_datos:
            self.treemap.insert("", "end", values=dato)

    def viz_alumno(self): 
        self.cleanWindow()

            # Configuración de estilo para el Treeview
        style = ttk.Style()
        style.theme_use("clam")  # Usar tema "clam" como base para la personalización
        # Color más oscuro para los encabezados
        style.configure("Treeview.Heading", background= "#7B2973", font = self.fuente_Subtitulo, foreground = self.color_blanco)
        # self.treemap
        self.treemap = ttk.Treeview(self.root, columns=("Grupo", "Matricula", "Nombre"), show="headings", style="Treeview")
        self.treemap.heading("Grupo", text="Grupo", anchor=tk.CENTER)
        self.treemap.heading("Matricula", text="Matricula")
        self.treemap.heading("Nombre", text="Nombre")
        self.treemap.grid(row=5, column=0, columnspan=12, rowspan = 4, sticky="nsew")

        botones_treemap = [
        ("Agregar Alumno", lambda: alumnos_funciones.agregar_alumnos(self), 0),
        ("Editar Alumno", lambda: alumnos_funciones.editar_alumno(self), 6),
        ]

        btn_salir = tk.Button(self.root, text="Salir", command=self.create_widgets, bg=self.color_gris, fg="white", font=self.fuente_Subtitulo)
        btn_salir.grid(row=18, column=0, columnspan=2, sticky="nswe")


        for text, command, col in botones_treemap:
            btn = tk.Button(self.root, text=text, command=command, bg=self.color_gris, fg="white", font=self.fuente_Subtitulo)
            btn.grid(row=9, column=col, columnspan=6, sticky="nswe")

        lista_alumnos = alumnos_funciones.obtener_alumnos(self.ip_conn)

        for dato in lista_alumnos:
            self.treemap.insert("", "end", values=dato)

    def viz_sistema(self): 
        self.cleanWindow()

            # Configuración de estilo para el Treeview
        style = ttk.Style()
        style.theme_use("clam")  # Usar tema "clam" como base para la personalización
        # Color más oscuro para los encabezados
        style.configure("Treeview.Heading", background= "#7B2973", font = self.fuente_Subtitulo, foreground = self.color_blanco)
        # self.treemap
        self.treemap = ttk.Treeview(self.root, columns=("P1", "P2", "P3"), show="headings", style="Treeview")
        self.treemap.heading("P1", text="P1", anchor=tk.CENTER)
        self.treemap.heading("P2", text="P2")
        self.treemap.heading("P3", text="P3")
        self.treemap.grid(row=5, column=0, columnspan=12, rowspan = 4, sticky="nsew")


        botones_treemap = [
        ("Agregar Sistema", lambda: sistemas_funciones.agregar_sistema(self), 0),
        ("Editar Sistema", lambda: sistemas_funciones.editar_sistema(self), 6),
        ]

        for text, command, col in botones_treemap:
            btn = tk.Button(self.root, text=text, command=command, bg=self.color_gris, fg="white", font=self.fuente_Subtitulo)
            btn.grid(row=9, column=col, columnspan=6, sticky="nswe")


        lista_sistema = sistemas_funciones.obtener_sistema(self.ip_conn)
        for dato in lista_sistema:
            self.treemap.insert("", "end", values=dato)

        btn_salir = tk.Button(self.root, text="Salir", command=self.create_widgets, bg=self.color_gris, fg="white", font=self.fuente_Subtitulo)
        btn_salir.grid(row=18, column=0, columnspan=2, sticky="nswe")


    def get_selected_option(self,event,combo_box):
        self.selected_option = combo_box.get()

        print(self.selected_option)

    def laboratorio_opciones(self):
        self.cleanWindow()
        practicas_data  = phpFuncs.get_Practicas(self.ip_conn)

        practicas_existentes = [item['numero_practica'] for item in practicas_data]
        practicas_existentes = list(set(practicas_existentes))
        self.crear_practica = tk.Button(self.root, text="Crear Práctica",fg = self.color_blanco,bg= self.color_gris,font=self.fuente_Titulo,command=lambda: practicas_funciones.crear_practica(self),width=15, height=3, justify='center', wraplength=200)
        self.crear_practica.grid(row=9,column=4,sticky = "nswe")
        self.ver_practica = tk.Button(self.root, text="Visualizar Prácticas",fg = self.color_blanco,bg= self.color_gris,font=self.fuente_Titulo,command=self.viz_laboratorio,width=15, height=3, justify='center', wraplength=200)
        self.ver_practica.grid(row=9,column=8,sticky = "nswe")

        combo_box = ttk.Combobox(self.root, font=self.fuente_Titulo,state='readonly')
        combo_box['values'] = practicas_existentes
        combo_box.grid(row=10,column=8)
        combo_box.bind("<<ComboboxSelected>>", lambda event: self.get_selected_option(event, combo_box))


        btn_salir = tk.Button(self.root, text="Salir", command=self.create_widgets, bg=self.color_gris, fg="white", font=self.fuente_Subtitulo)
        btn_salir.grid(row=18, column=0, columnspan=2, sticky="nswe")

    def viz_laboratorio(self): 
        self.cleanWindow()

        style = ttk.Style()
        style.theme_use("clam")  # Usar tema "clam" como base para la personalización
        # Color más oscuro para los encabezados
        style.configure("Treeview.Heading", background= "#7B2973", font = self.fuente_Subtitulo, foreground = self.color_blanco)
        # self.treemap
        self.treemap = ttk.Treeview(self.root, columns=("Alumno", "Sistema", "Numero de Practica"), show="headings", style="Treeview")
        self.treemap.heading("Alumno", text="Alumno", anchor=tk.CENTER)
        self.treemap.heading("Sistema", text="Sistema")
        self.treemap.heading("Numero de Practica", text="Numero de Practica")
        self.treemap.grid(row=5, column=0, columnspan=12, rowspan = 4, sticky="nsew")

        lista_practicas = practicas_funciones.obtener_practicas_by_numero(self)
        for dato in lista_practicas:
            self.treemap.insert("", "end", values=dato)

        btn_salir = tk.Button(self.root, text="Salir", command=self.create_widgets, bg=self.color_gris, fg="white", font=self.fuente_Subtitulo)
        btn_salir.grid(row=18, column=0, columnspan=2, sticky="nswe")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    lab_window = lab_app("lab_window",400,400)
    lab_window.run()