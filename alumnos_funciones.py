from tkinter import * 
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import phpFuncs

# Función asociada al botón "Agregar Componente"

def actualizar_treemap(lista_datos,treemap):
    for item in treemap.get_children():
        treemap.delete(item)
    for dato in lista_datos:
        treemap.insert("", "end", values=dato)

def obtener_alumnos(ip_conn):
    alumnos = phpFuncs.select_Alumnos(ip_conn)

    lista_alumnos = []

    for alumno in alumnos: 

        alumno_dato = []

        alumno_dato.append(alumno['grupo'])
        alumno_dato.append(alumno['matricula'])
        alumno_dato.append(alumno['nombre'])
        alumno_dato.append(alumno['idalumno'])

        print(alumno_dato)

        lista_alumnos.append(alumno_dato)

    return lista_alumnos


def agregar_alumnos(configs):
    print(configs)

    def agregar():
        grupo = entry_grupo.get()
        matricula = entry_matricula.get()
        nombre = entry_nombre.get()
        
        if grupo == "" or matricula == "" or nombre == "":
            messagebox.showwarning("Aviso", "Alguno de los campos está vacío")
            return
        else: 

            msg_json = {'nombre':nombre,'grupo':grupo, 'matricula': matricula}

            phpFuncs.insertar_alumno(configs.ip_conn,msg_json)

            lista_alumnos = obtener_alumnos(configs.ip_conn)
            actualizar_treemap(lista_alumnos,configs.treemap)
            ventana_agregar.destroy()
            



    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Alumno")
    ventana_agregar.config(bg=configs.color_azul)

    # Campos de entrada para el nuevo componente
    tk.Label(ventana_agregar, text="Grupo:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=0, column=0)
    entry_grupo = tk.Entry(ventana_agregar,font=configs.fuente_Entry)
    entry_grupo.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Matricula:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=1, column=0)
    entry_matricula = tk.Entry(ventana_agregar,font=configs.fuente_Entry)
    entry_matricula.grid(row=1, column=1)
    
    tk.Label(ventana_agregar, text="Nombre:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=2, column=0)
    entry_nombre = tk.Entry(ventana_agregar,font=configs.fuente_Entry)
    entry_nombre.grid(row=2, column=1)

    # Botón para agregar el componente
    btn_crear = tk.Button(ventana_agregar, text="Crear", command=agregar,bg=configs.color_morado,fg=configs.color_blanco)
    btn_crear.grid(row=3, column=0, columnspan=2)


def editar_alumno(configs):
    selected_item = configs.treemap.selection()
    
    def guardar_cambios():

        nuevo_grupo = entry_grupo.get()
        nueva_matricula = entry_matricula.get()
        nuevo_nombre = entry_nombre.get()
        
        if grupo == "" or matricula == "" or nombre == "":
            messagebox.showwarning("Aviso", "Alguno de los campos está vacío")
            return
        else:
            lista_alumnos = obtener_alumnos(configs.ip_conn)
            for alumno in lista_alumnos:
                if alumno[2] == nombre:
                    id_alumno = alumno[3]

            msg_json = {'nombre':nuevo_nombre,'grupo':nuevo_grupo, 'matricula': nueva_matricula,'id_alumno':id_alumno}
            print(f"message update {msg_json}")
            phpFuncs.update_Alumno(configs.ip_conn,msg_json)
            lista_alumnos = obtener_alumnos(configs.ip_conn)
            actualizar_treemap(lista_alumnos,configs.treemap)
            ventana_editar.destroy()
            
            
    if selected_item:
        grupo = configs.treemap.item(selected_item, 'values')[0]
        matricula = configs.treemap.item(selected_item,'values')[1]
        nombre = configs.treemap.item(selected_item, 'values')[2]
             
        ventana_editar = tk.Toplevel()
        ventana_editar.title("Editar Componente")
        ventana_editar.config(bg=configs.color_azul)

        # Campos de entrada para editar el componente
        tk.Label(ventana_editar, text="Grupo:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=0, column=0)
        entry_grupo = tk.Entry(ventana_editar,font=configs.fuente_Entry)
        entry_grupo.insert(0,grupo)
        entry_grupo.grid(row=0, column=1)
        
        tk.Label(ventana_editar, text="Matricula:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=1, column=0)
        entry_matricula = tk.Entry(ventana_editar,font=configs.fuente_Entry)
        entry_matricula.insert(0,matricula)
        entry_matricula.grid(row=1, column=1)

        tk.Label(ventana_editar, text="Nombre:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=2, column=0)
        entry_nombre = tk.Entry(ventana_editar,font=configs.fuente_Entry)
        entry_nombre.insert(0,nombre)
        entry_nombre.grid(row=2, column=1)

        btn_crear = tk.Button(ventana_editar, text="Guardar Cambios", command=lambda: guardar_cambios(),bg=configs.color_morado,fg=configs.color_blanco)
        btn_crear.grid(row=3, column=0, columnspan=2)


    else:
        messagebox.showerror("Error", "Por favor selecciona un componente para editar")