import json 
import requests 
import random 
from tkinter import messagebox

import phpFuncs
import practicas_funciones
import sistemas_funciones
import alumnos_funciones

def crear_practica(configs):

    lista_num_practicas = phpFuncs.get_numero_practica(configs.ip_conn)

    if lista_num_practicas == []: 
        numero_practica = 1
    else: 
        max_value = max(lista_num_practicas, key=lambda x: x['numero_practica'])

        print(max_value)
        numero_practica =  int(max_value['numero_practica']) + 1

    print(numero_practica)

    lista_alumnos = alumnos_funciones.obtener_alumnos(configs.ip_conn)

    lista_sistemas = sistemas_funciones.obtener_sistema(configs.ip_conn)

    for alumno in lista_alumnos: 
        random_num = random.randint(0,len(lista_sistemas)-1)
        id_sistema = lista_sistemas[random_num][3]
        id_alumno = alumno[3]

        msg_json = {'id_alumno':id_alumno,'id_sistema':id_sistema, 'numero_practica': numero_practica}

        phpFuncs.insertar_practicas(configs.ip_conn,msg_json)

    
    messagebox.showinfo("Proceso", "El proceso se ha completado")


def obtener_practicas(ip_conn):
    practicas = phpFuncs.get_Practicas(ip_conn)

    lista_practicas = []

    for practica in practicas: 

        practica_dato = []

        practica_dato.append(practica['idalumno'])
        practica_dato.append(practica['idsistema'])
        practica_dato.append(practica['numero_practica'])
        practica_dato.append(practica['idlab'])

        print(practica_dato)

        lista_practicas.append(practica_dato)

    return lista_practicas

def obtener_practicas_by_numero(configs):
    practicas = phpFuncs.get_InfoByNumero(configs.ip_conn,configs.selected_option)

    lista_practicas = []

    for practica in practicas: 

        practica_dato = []
        print(f"Practica info: {practica}")
        print(f"id_alumno: {practica['idalumno']}")
        alumno_dato = phpFuncs.get_AlumnoById(configs.ip_conn,practica['idalumno'])
        practica_dato.append(alumno_dato[0]['nombre'])

        print(f"id_sistema: {practica['idsistema']}")
        sistema_dato = phpFuncs.get_SistemaById(configs.ip_conn,practica['idsistema'])
        sistema = [[item['p1'], item['p2'],item['p3']] for item in sistema_dato]
        #print(key_name_values)

        practica_dato.append(sistema)
        practica_dato.append(practica['numero_practica'])

        print(practica_dato)

        lista_practicas.append(practica_dato)

    return lista_practicas

        
