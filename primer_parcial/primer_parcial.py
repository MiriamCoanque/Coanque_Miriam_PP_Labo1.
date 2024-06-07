'''El programa contará con el siguiente menú:
1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos
del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
servicios.
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
7) Salir.'''

from biblioteca import *
from json import *

def menu():
    print('''            
            1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos del mismo.
            2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los servicios.
            3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
            4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan servicios del tipo seleccionado.
            5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por descripción de manera ascendente.
            6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
            7) Salir.''')
    opcion = int(input("opción: "))
    return opcion

def pedir_tipo():
    tipo = input("Ingrese el tipo: ")
    return tipo

def mostrar_tipo(lista:list):
    for e_lista in lista:
        print(e_lista)

def filtrar_tipo(lista: list, tipo: str) -> list:
    '''
    recibe una lista de diccionarios en la cual trabajo y tipo el cual uso para filtrar
    retorna una lista de diccionarios filtrado con el tipo'''

    nueva_lista = []
    for e_lista in lista:
        if e_lista['tipo'] == tipo:
            nueva_lista.append(e_lista)
    return nueva_lista 

while True:
    opcion = menu()
    if opcion == 1:
        nombre = pedir_nombre()
        lista = cargar_archivo("primer_parcial\data.json")
        mostrar_archivo(lista,nombre)

    elif opcion == 2:
        lista = cargar_archivo("primer_parcial\data.json")
        mostrar_todos_los_datos(lista)

    elif opcion == 3:
        lista = cargar_archivo("primer_parcial\data.json")
        calcular_totales(lista,"cantidad","precioUnitario")
    elif opcion == 4:
        tipo = pedir_tipo()
        lista = cargar_archivo("primer_parcial\data.json")
        filtrar_tipo(lista,tipo)
        mostrar_tipo(filtrar_tipo)
    elif opcion == 5:
        lista = cargar_archivo("primer_parcial\data.json")
        ordenar_lista_por_descripcion(lista,"ascendente")
    elif opcion == 6:
        pass
    elif opcion == 7:
        despedir()
        break