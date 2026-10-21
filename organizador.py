
#organizer.py
from pathlib import Path


def comprobar_ruta(ruta):
    ruta = Path(ruta)
    if ruta.exists():
        return True, ruta
    else:
        return False, ruta



# verifica los archivos existentes
def verifica_archivos_existentes(ruta_de_trabajo):
    archivos = []
    for a in ruta_de_trabajo.iterdir():
        if a.is_file() and a.suffix.lower() not in ['.pyc', '.pyo', '.py', '']:
            archivos.append(a)
    return archivos


# devuelve los nombres de las extensiones existentes
def extenciones_existentes(archivos):
    return {a.suffix.lower()[1:] for a in archivos}


# crea las carpetas de las extensiones existentes
def crear_carpeta(extensiones, ruta_de_trabajo):
    for c in extensiones:
        carpeta = ruta_de_trabajo / c
        carpeta.mkdir(exist_ok=True)

# ordena los archivos y carpetas alfabeticamente
def ordenar_alfabeticamente(carpetas, archivos):
    archivos_ordenados = sorted(archivos, key=lambda a: (a.suffix.lower(), a.name))
    carpetas_ordenadas = sorted(carpetas)
    return archivos_ordenados, carpetas_ordenadas


# muestra el plan de acciones a procesar
# ame los joins
def mostrar_plan(carpetas_ordenadas, archivos_ordenados, ruta_de_trabajo):

    print (f' carpeta de trabajo:\n {ruta_de_trabajo}\n')

    print(f'''carpetas a crear:
{'\n'.join(map(str, carpetas_ordenadas))}

archivos existentes a mover: {len(archivos_ordenados)}

nombres de archivos a mover:
{'\n'.join(a.name for a in archivos_ordenados)}

resultado:
{'\n'.join(f'{a.name} -> {ruta_de_trabajo / a.suffix.lower()[1:] / a.name}' for a in archivos_ordenados)}
''')

def organizar(destino, origen, ruta_de_trabajo):
    for a in origen:
        for d in destino:
            if a.suffix.lower()[1:] == d:
                a.rename(ruta_de_trabajo / d / a.name)


def diccionario_con_valores(rutas):
    archivos = verifica_archivos_existentes(rutas)
    extenciones = extenciones_existentes(archivos)
    archivos_ordenados, carpetas_ordenadas = ordenar_alfabeticamente(extenciones, archivos)
    return {
    "ruta": rutas,
    "archivos": archivos,
    "extenciones": extenciones,
    "archivos_ordenados": archivos_ordenados,
    "carpetas_ordenadas": carpetas_ordenadas
}

#crear_carpeta()
#organizar()

