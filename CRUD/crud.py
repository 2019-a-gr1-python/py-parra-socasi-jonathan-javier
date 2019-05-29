import os

def listar():

    print('LISTADO DE PRODUCTOS DISPONIBLES')
    try:
        path="./autos.txt"
        archivo_a_leer = open(path,mode='r')
        for index , line in enumerate(archivo_a_leer.readlines()): 
            print(f'{index} {line}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar():

    print('ELIMINAR')
    listar()
    registro_a_eliminar = input('Ingrese numero de registro a eliminar: ')
    path="./autos.txt"
    archivo_a_leer = open(path,mode='r')
    arreglo_nuevo=archivo_a_leer.readlines()
    arreglo_nuevo.pop(int(registro_a_eliminar))
    print(f'ESTOOO ES ARREGLOOO A GUARDAR {arreglo_nuevo}')
    archivo_a_leer.close()
    os.remove('autos.txt')
    archivo_a_crear=open(path,mode='a+')     
    archivo_a_crear.writelines(arreglo_nuevo)
    archivo_a_crear.close()    


def crear():
            
    marca= input('Ingrese marca del dispositivo movil:  ')
    modelo= input(f'Ingrese el modelo del dispositivo movil marca {marca}:  ')
    precio= input(f'Ingrese precio del dispositivo {marca}-{modelo}:  ')    
    try:
        path="./autos.txt"
        archivo_a_escribir = open(path,mode='a+')
        archivo_a_escribir.writelines(f'{marca}     {modelo}     {precio}\n')
        archivo_a_escribir.close() 
    except Exception as error:
        return f'Error en el archivo: {error}'
    return archivo_a_escribir

def switch_accion(): 
    
    accionAbuscar=input('Ingrese numero de la accion a realizar \n 1.- Crear \n 2.- Listar \n 3.- Eliminar \n')
    return { 
        1:crear(),
        2:listar(),
        3:eliminar(),
        }[accionAbuscar]
            
switch_accion()