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

def obtener_sistema(ip_conn):
    sistemas = phpFuncs.select_Sistema(ip_conn)

    lista_sistemas = []

    for sistema in sistemas: 

        sistema_dato = []

        sistema_dato.append(sistema['p1'])
        sistema_dato.append(sistema['p2'])
        sistema_dato.append(sistema['p3'])
        sistema_dato.append(sistema['idsistema'])

        print(sistema_dato)

        lista_sistemas.append(sistema_dato)

    return lista_sistemas


def agregar_sistema(configs):
    print(configs)

    def agregar():
        p1 = entry_p1.get()
        p2 = entry_p2.get()
        p3 = entry_p3.get()
        
        if p1 == "" or p2 == "" or p3 == "":
            messagebox.showwarning("Aviso", "Alguno de los campos está vacío")
            return
        else: 

            msg_json = {'p1':p1,'p2':p2, 'p3': p3}

            phpFuncs.insertar_sistema(configs.ip_conn,msg_json)

            lista_alumnos = obtener_sistema(configs.ip_conn)
            actualizar_treemap(lista_alumnos,configs.treemap)
            ventana_agregar.destroy()
            
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Alumno")
    ventana_agregar.config(bg=configs.color_azul)

    # Campos de entrada para el nuevo componente
    tk.Label(ventana_agregar, text="P1:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=0, column=0)
    entry_p1 = tk.Entry(ventana_agregar,font=configs.fuente_Entry)
    entry_p1.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="P2:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=1, column=0)
    entry_p2 = tk.Entry(ventana_agregar,font=configs.fuente_Entry)
    entry_p2.grid(row=1, column=1)
    
    tk.Label(ventana_agregar, text="P3:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=2, column=0)
    entry_p3 = tk.Entry(ventana_agregar,font=configs.fuente_Entry)
    entry_p3.grid(row=2, column=1)

    # Botón para agregar el componente
    btn_crear = tk.Button(ventana_agregar, text="Crear", command=agregar,bg=configs.color_morado,fg=configs.color_blanco)
    btn_crear.grid(row=3, column=0, columnspan=2)


def editar_sistema(configs):
    selected_item = configs.treemap.selection()
    
    def guardar_cambios():

        nuevo_p1 = entry_p1.get()
        nuevo_p2 = entry_p2.get()
        nuevo_p3 = entry_p3.get()
        
        if nuevo_p1 == "" or nuevo_p2 == "" or nuevo_p3 == "":
            messagebox.showwarning("Aviso", "Alguno de los campos está vacío")
            return
        else:
            lista_sistemas = obtener_sistema(configs.ip_conn)
            for sistema in lista_sistemas:
                if sistema[0] == p1 and sistema[1] == p2 and sistema[2] == p3:
                    id_sistema = sistema[3]

            msg_json = {'p1':nuevo_p1,'p2':nuevo_p2, 'p3':nuevo_p3,'id_sistema':id_sistema}
            print(f"message update {msg_json}")
            phpFuncs.update_Sistema(configs.ip_conn,msg_json)
            lista_sistemas = obtener_sistema(configs.ip_conn)
            actualizar_treemap(lista_sistemas,configs.treemap)
            ventana_editar.destroy()
            
            
    if selected_item:
        p1 = configs.treemap.item(selected_item, 'values')[0]
        p2 = configs.treemap.item(selected_item,'values')[1]
        p3 = configs.treemap.item(selected_item, 'values')[2]
             
        ventana_editar = tk.Toplevel()
        ventana_editar.title("Editar Componente")
        ventana_editar.config(bg=configs.color_azul)

        # Campos de entrada para editar el componente
        tk.Label(ventana_editar, text="P1:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=0, column=0)
        entry_p1 = tk.Entry(ventana_editar,font=configs.fuente_Entry)
        entry_p1.insert(0,p1)
        entry_p1.grid(row=0, column=1)
        
        tk.Label(ventana_editar, text="P2:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=1, column=0)
        entry_p2 = tk.Entry(ventana_editar,font=configs.fuente_Entry)
        entry_p2.insert(0,p2)
        entry_p2.grid(row=1, column=1)

        tk.Label(ventana_editar, text="P3:",bg=configs.color_azul,fg=configs.color_blanco,font=configs.fuente_Entry).grid(row=2, column=0)
        entry_p3 = tk.Entry(ventana_editar,font=configs.fuente_Entry)
        entry_p3.insert(0,p3)
        entry_p3.grid(row=2, column=1)

        btn_crear = tk.Button(ventana_editar, text="Guardar Cambios", command=lambda: guardar_cambios(),bg=configs.color_morado,fg=configs.color_blanco)
        btn_crear.grid(row=3, column=0, columnspan=2)


    else:
        messagebox.showerror("Error", "Por favor selecciona un componente para editar")