#panel.py
import os
import subprocess
from organizador import comprobar_ruta, diccionario_con_valores, mostrar_plan
from pathlib import Path

def limpiar():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

def menu_inicio():
    diccionario = {
        "ruta": None,
        "archivos": [],
        "extenciones": [],
        "archivos_ordenados": [],
        "carpetas_ordenadas": []
    }
    limpiar()
    while True:
        limpiar()
        print(f'''
================================
    ORGANIZADOR DE ARCHIVOS
================================ 
carpeta de trabajo actual: 
{"".join(str(diccionario['ruta']) if diccionario['ruta'] else "no se configuro")}
================================ 
    1. Elegir carpeta de trabajo
    2. Configurar exclusiones
    3. Incluir subcarpetas
    4. Previsualizar organización
    5. Organizar archivos
    6. Salir
        ''')
        
        try:
            ingreso = int(input('Opción: '))
            if ingreso == 1:
                retorno = menu_1()
                if retorno:
                    diccionario = diccionario_con_valores(retorno)
                continue
            elif ingreso == 2:
                pass
            elif ingreso == 3:
                pass
            elif ingreso == 4:
                limpiar()
                if not diccionario['ruta']:
                    print("\nno se configuro la carpeta de trabajo\n")
                    seleccion = input("queres seleccionar la carpeta de trabajo en la que te encuentras? (s/n): ")
                    if seleccion.lower() == 's':
                        limpiar()
                        diccionario = diccionario_con_valores(Path.cwd())
                        print("carpeta de trabajo configurada")
                        input("presione una tecla Previsualizar organización...")
                        limpiar()
                        mostrar_plan(diccionario['carpetas_ordenadas'], diccionario['archivos_ordenados'], diccionario['ruta'])
                        input("Presione una tecla para continuar...")
                        continue
                    else:
                        continue
                else:
                    mostrar_plan(diccionario['carpetas_ordenadas'], diccionario['archivos_ordenados'], diccionario['ruta'])
                    continue
            elif ingreso == 5:
                pass
            elif ingreso == 6:
                limpiar()
                break
        except ValueError:
            limpiar()
            print('Opción inválida')
            input('Presione una tecla para continuar...')
            continue

def menu_1():
    limpiar()
    print("Ejemplo: C:/Users/nico/Escritorio/documentos")
    ruta_ingresada = input("Ruta de la carpeta de trabajo: ")

    existe, ruta = comprobar_ruta(ruta_ingresada)
    if existe and ruta.is_dir():
        while True:
            print(f'''Carpeta de trabajo elegida:
{str(ruta)}''')
            confirmacion = input("¿Desea confirmar? (s/n): ")
            if confirmacion.lower() == 's':
                print("Carpeta de trabajo configurada")
                return ruta # devuelve la ruta de la carpeta de trabajo
            elif confirmacion.lower() == 'n':
                limpiar()
                print("Opción cancelada")
                input("Presione una tecla para continuar...")
                return
    elif existe and ruta.is_file():
        limpiar()
        print ("ERROR")
        print("la ruta ingresada es un archivo")
        input("Presione una tecla para continuar...")
    else:
        limpiar()
        print("La ruta ingresada no existe")
        confirmacion = input("desea crear la carpeta? (s/n): ")
        if confirmacion.lower() == 's':
            ruta.mkdir(exist_ok=True, parents=True)
            limpiar()
            print("Carpeta creada y configurada")
            print("ahora podes poner los archivos en la carpeta y ejecutar el organizador")
            input("presione una tecla para continuar...")
            return ruta
        elif confirmacion.lower() == 'n':
            limpiar()
            print("Opción cancelada")
            input("Presione una tecla para continuar...")
        else:
            limpiar()
            print("Opción inválida")
            input("Presione una tecla para continuar...")


menu_inicio()















