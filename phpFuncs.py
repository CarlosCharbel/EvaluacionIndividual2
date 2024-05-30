import json 
import requests

def insertar_alumno(ip,json_dict):
    payload = json.dumps(json_dict)  # Convierte el diccionario JSON a formato de cadena JSON
    query = f"http://{ip}/php_eval/insertar_alumno.php"  # Construye la URL de la consulta
    res = requests.post(query, data=payload)  # Realiza una solicitud POST a la URL con los datos JSON
    response = res.text  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)

    return response  # Retorna la respuesta

def check_alumno(ip,nombre,matricula): 
    query = f"http://{ip}/php_eval/check_alumno.php?nombre={nombre}&matricula={matricula}"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    response = res.json()
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta

def select_Alumnos(ip):
    query = f"http://{ip}/php_eval/select_alumnos.php"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    print(res.text)
    response = res.json()  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta

def update_Alumno(ip,msg_json):
    payload = json.dumps(msg_json)  # Convierte el diccionario JSON a formato de cadena JSON
    query = f"http://{ip}/php_eval/update_alumno.php"  # Construye la URL de la consulta
    res = requests.post(query, data=payload)  # Realiza una solicitud POST a la URL con los datos JSON
    response = res.text  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)

def get_AlumnoById(ip,id): 
    query = f"http://{ip}/php_eval/select_alumno_id.php?id={id}"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    response = res.json()
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta

#######################################################################33
def select_Sistema(ip):
    query = f"http://{ip}/php_eval/select_sistemas.php"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    response = res.json()  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta

def insertar_sistema(ip,json_dict):
    payload = json.dumps(json_dict)  # Convierte el diccionario JSON a formato de cadena JSON
    query = f"http://{ip}/php_eval/insertar_sistema.php"  # Construye la URL de la consulta
    res = requests.post(query, data=payload)  # Realiza una solicitud POST a la URL con los datos JSON
    response = res.text  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)

    return response  # Retorna la respuesta

def update_Sistema(ip,msg_json):
    payload = json.dumps(msg_json)  # Convierte el diccionario JSON a formato de cadena JSON
    query = f"http://{ip}/php_eval/update_sistema.php"  # Construye la URL de la consulta
    res = requests.post(query, data=payload)  # Realiza una solicitud POST a la URL con los datos JSON
    response = res.text  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)

def get_SistemaById(ip,id): 
    query = f"http://{ip}/php_eval/select_sistema_id.php?id={id}"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    response = res.json()
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta
###################################

def get_Practicas(ip):
    query = f"http://{ip}/php_eval/select_practicas.php"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    print(res.text)
    response = res.json()  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta

def get_numero_practica(ip):
    query = f"http://{ip}/php_eval/get_numero_practica.php"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    print(res.text)
    response = res.json()  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta

def insertar_practicas(ip,json_dict):
    payload = json.dumps(json_dict)  # Convierte el diccionario JSON a formato de cadena JSON
    query = f"http://{ip}/php_eval/insertar_practica.php"  # Construye la URL de la consulta
    res = requests.post(query, data=payload)  # Realiza una solicitud POST a la URL con los datos JSON
    response = res.text  # Obtiene el texto de la respuesta
    print(response)  # Imprime la respuesta (para depuración)

    return response  # Retorna la respuesta

def get_InfoByNumero(ip,numero): 
    query = f"http://{ip}/php_eval/select_practica_numero.php?numero={numero}"  # Construye la URL de la consulta
    res = requests.get(query)  # Realiza una solicitud GET a la URL
    response = res.json()
    print(response)  # Imprime la respuesta (para depuración)
    return response  # Retorna la respuesta