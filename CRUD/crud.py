import os

path = "./autos.txt"

def leer_archivo(path):
    archivo_a_leer = open(path,mode='r')
    return archivo_a_leer

def escribir_archivo(path, contenido):
    archivo_a_escribir = open(path,mode='a+')
    archivo_a_escribir.writelines(contenido)
    archivo_a_escribir.close()
    return archivo_a_escribir 

def eliminar():    
    listar()
    registro_a_eliminar = input('Ingrese numero de registro a eliminar: ')   
    id_registro = int(registro_a_eliminar) 
    arreglo_nuevo=leer_archivo(path).readlines()
    arreglo_nuevo.pop(id_registro)    
    os.remove('autos.txt')
    escribir_archivo(path,arreglo_nuevo)
    listar()
    switch_accion()    

def listar():
    print('LISTADO DE PRODUCTOS DISPONIBLES')
    try:
        lista_autos = leer_archivo(path)
        for line in enumerate(lista_autos.readlines()): 
            print(line)
        lista_autos.close()
    except Exception as error:
        print('Error: ', {error})

def crear():
    marca= raw_input("Ingrese marca del auto:  ")
    modelo= raw_input("Ingrese el modelo del auto de marca " + marca + " ")
    color= raw_input("Ingrese el color del auto con " + marca + " y " + modelo + " ")
    contenido = marca + "   " +  modelo + "   " + color + "\n"
    try:                
        registrar = escribir_archivo(path,contenido)
        print('REGISTRO CREADO CON EXITO!')
        listar()
        switch_accion()
    except Exception as error:
        return "Error en el archivo: {error}"
    return registrar
            
def modificar():
    listar()
    registro = raw_input("Ingresar el registro a modificar")    
    marca= raw_input("Ingrese marca del auto:  ")
    modelo= raw_input("Ingrese el modelo del auto de marca " + marca + " ")
    color= raw_input("Ingrese el color del auto con " + marca + " y " + modelo + " ")
    id_registro = int(registro)
    contenido = marca + "   " +  modelo + "   " + color + "\n"
    try:            
        print(id_registro, contenido)
        registro_modificar = leer_archivo(path).readlines()        
        registro_modificar[id_registro] = contenido
        os.remove('autos.txt')
        registrar_modificacion = escribir_archivo(path,registro_modificar)
        registrar_modificacion.close()  
        listar()        
        switch_accion()
    except Exception as error:
        print('Error: {error}')

def switch_accion():     
    accionAbuscar = raw_input('Ingrese numero de la accion a realizar \n 1.- Crear \n 2.- Listar \n 3.- Modificar \n 4.- Eliminar \n')
    switcher = {
        1: crear(),
        2: listar(),
        3: modificar(),
        4: eliminar()
    }
    return switcher.get(accionAbuscar, "nothing") 

switch_accion()