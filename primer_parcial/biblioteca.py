import json

def pedir_nombre():
    nombre = input("Ingrese el nombre: ")
    return nombre

def cargar_archivo(nombre:str)->list:
    try:
        with open(nombre, "r") as archivo:
            resultado = json.load(archivo)

        return resultado
    except FileNotFoundError:
        print("Archivo no encontrado")
        return False

def mostrar_todos_los_datos(lista:list):
    for e_lista in lista:
        print(f"ID: {e_lista['id_servicio']}\tDescripción: {e_lista['descripcion']}\tTipo: {e_lista['tipo']}\tPrecio Unitario: {e_lista['precioUnitario']}\tCantidad: {e_lista['cantidad']}\tTotal servicio: {e_lista['totalServicio']}")

def despedir():
    print("Ha elegido 'Salir' :) ")


def mostrar_archivo(lista: list, nombre_lista: str):
    '''recibe una lista tipo lista con la que trabajo y un nombre que le asignaré a dicha lista'''
    print(f"Nombre: {nombre_lista}")
    print(lista)

def calcular_totales(lista: list,clave1:str,clave2:str):
    '''recibe una lista con la que trabajaré
    clave1 para obtener la cantidad
    calve2 para obtener el preciounitario'''
    calcular_total = lambda elemento: elemento[clave1] * elemento[clave2]
    for e_lista in lista:
        e_lista['totalServicio'] = calcular_total(e_lista)

def filtrar_tipo(lista: list, tipo: str) -> list:
    '''
    recibe una lista de diccionarios en la cual trabajo y tipo el cual uso para filtrar
    retorna una lista de diccionarios filtrado con el tipo'''

    nueva_lista = []
    for e_lista in lista:
        if e_lista['tipo'] == tipo:
            nueva_lista.append(e_lista)
    return nueva_lista
    
def ordenar_lista_por_descripcion(lista: list, tipo: str) -> list:

    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if tipo == "ascendente" and lista[i]['descripcion'] > lista[j]['descripcion']:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
            elif tipo == "descendente" and lista[i]['descripcion'] < lista[j]['descripcion']:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista
        


