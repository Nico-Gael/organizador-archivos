from pathlib import Path

# ruta base de la carpeta de trabajo
CARPETA_BASE = Path.cwd()

# verifica los archivos existentes
def verifica_archivos_existentes():
    archivos = []
    carpeta = CARPETA_BASE
    for a in carpeta.iterdir():
        if a.is_file() and a.suffix.lowe() not in ['.pyc', '.pyo', '.py', '']:
            archivos.append(a)
    return archivos


# devuelve los nombres de las extensiones existentes
def extenciones_existentes():
    archivos = verifica_archivos_existentes()
    return {a.suffix.lower()[1:] for a in archivos}


# crea las carpetas de las extensiones existentes
def crear_carpeta():
    nombres = extenciones_existentes()
    for c in nombres:
        carpeta = CARPETA_BASE / c
        carpeta.mkdir(exist_ok=True)

# ordena los archivos y carpetas alfabeticamente
def ordenar_alfabeticamente():
    archivos = verifica_archivos_existentes()
    carpetas = extenciones_existentes()

    archivos_ordenados = sorted(archivos, key=lambda a: (a.suffix.lower(), a.name))
    carpetas_ordenadas = sorted(carpetas)

    return archivos_ordenados, carpetas_ordenadas


# muestra el plan de acciones a procesar
# ame los joins
def mostrar_plan():
    archivos_ordenados, carpetas_ordenadas = ordenar_alfabeticamente()

    print(f'''1. Crear carpetas de extensiones existentes:

carpetas a crear:
{'\n'.join(map(str, carpetas_ordenadas))}

archivos existentes a mover: {len(archivos_ordenados)}

nombres de archivos a mover:
{'\n'.join(a.name for a in archivos_ordenados)}

resultado:
{'\n'.join(f'{a.name} -> {a.parent / a.suffix.lower()[1:] / a.name}' for a in archivos_ordenados)}
''')

def organizar():
    origen = verifica_archivos_existentes()
    destino = extenciones_existentes()
    for a in origen:
        for d in destino:
            if a.suffix.lower()[1:] == d:
                a.rename(CARPETA_BASE / d / a.name)


mostrar_plan()
#crear_carpeta()
#organizar()