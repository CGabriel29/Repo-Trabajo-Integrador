import csv
import os
import unicodedata  # Se importa para manejar acentos

#Se define el encabezado y los continentes que serán válidos para los continentes.

ARCHIVO = "paises.csv"
ENCABEZADO = ["nombre", "poblacion", "superficie", "continente"]
CONTINENTES_VALIDOS = ["América", "Asia", "Europa", "África", "Oceanía", "Antártida"]

# Función auxiliar para quitar acentos de los textos
def quitar_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

#Si el archivo paises.csv no existe se crea.

def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8", newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
            escritor.writeheader()
        print("Archivo creado correctamente con encabezado:", ENCABEZADO)

#Carga los países y verifica que no hayan habido cambios en el encabezado, o errores en el contenido.

def cargar_paises():
    paises = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames != ENCABEZADO:
                print("Encabezado incorrecto. Se esperaba:", ENCABEZADO)
                return []
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print("Error en los datos:", fila)
        return paises
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []

#Muestra la lista completa de países del csv.

def mostrar_lista(lista):
    if not lista:
        print("No se encontraron resultados.")
    else:
        for p in lista:
            print(f"{p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")

#Carga la lista de paises y si coincide el nombre ingresado por el usuario muestra sus características.

def buscar_pais(nombre):
    paises = cargar_paises()
    nombre_normalizado = quitar_acentos(nombre.lower())
    resultados = [p for p in paises if nombre_normalizado in quitar_acentos(p["nombre"].lower())]
    mostrar_lista(resultados)

#Muestra la lista de paises según el continente.

def filtrar_por_continente(cont):
    paises = cargar_paises()
    filtrados = [p for p in paises if p["continente"].lower() == cont.lower()]
    mostrar_lista(filtrados)

#Muestra según un rango mínimo y máximo de población.

def filtrar_por_poblacion(min_pob, max_pob):
    paises = cargar_paises()
    filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
    mostrar_lista(filtrados)

#Muestra según un rango mínimo y máximo de superficie.

def filtrar_por_superficie(min_sup, max_sup):
    paises = cargar_paises()
    filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
    mostrar_lista(filtrados)

#Ordena los países según la clave seleccionada.

def ordenar_paises(clave, descendente=False):
    paises = cargar_paises()
    ordenados = sorted(paises, key=lambda x: x[clave], reverse=descendente)
    mostrar_lista(ordenados)

#Muestra estadisticas generales.

def estadisticas():
    paises = cargar_paises()
    if not paises:
        print("No hay datos para mostrar estadísticas.")
        return

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {promedio_pob:.2f}")
    print(f"Promedio de superficie: {promedio_sup:.2f}")

#Muestra los países por continente con un contador.

def cantidad_por_continente():
    paises = cargar_paises()
    conteo = {}
    for p in paises:
        cont = p["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1
    for cont, cantidad in conteo.items():
        print(f"{cont}: {cantidad} países")

#Validar entero

def ingresar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")

#Verificar que el rango maximo no sea menor al minimo.

def ingresar_rango(mensaje_min, mensaje_max):
    while True:
        min_val = ingresar_entero(mensaje_min)
        max_val = ingresar_entero(mensaje_max)
        if min_val > max_val:
            print("El valor mínimo no puede ser mayor que el máximo. Intente nuevamente.")
        else:
            return min_val, max_val

#Verificar continente.

def ingresar_continente():
    while True:
        cont = input("Ingrese el continente: ").strip().title()
        if cont in CONTINENTES_VALIDOS:
            return cont
        else:
            print(f"Continente inválido. Debe ser uno de: {', '.join(CONTINENTES_VALIDOS)}")

#Agrega un país con todas sus caracteristicas.

def agregar_pais():
    paises_existentes = cargar_paises()
    while True:
        nombre = input("Ingrese el nombre del país: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        nombre = nombre.title()
        if any(p["nombre"].lower() == nombre.lower() for p in paises_existentes):
            print(f"{nombre} ya existe en el archivo.")
            continue
        break

    poblacion = ingresar_entero("Ingrese la población: ")
    superficie = ingresar_entero("Ingrese la superficie (km²): ")
    continente = ingresar_continente()

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    with open(ARCHIVO, "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
        escritor.writerow(pais)
    print(f"{nombre} agregado.")

#Edita la característica seleccionada de un país.

def editar_pais():
    paises = cargar_paises()
    if not paises:
        print("No hay países en el archivo para editar.")
        return

    # Mostrar países
    mostrar_lista(paises)
    
    nombre_buscar = input("Ingrese el nombre del país a editar: ").strip().lower()
    coincidencias = [p for p in paises if nombre_buscar in p["nombre"].lower()]

    if not coincidencias:
        print("No se encontró ningún país con ese nombre.")
        return

    pais = coincidencias[0]

    #Mostrar las opciones a editar del encabezado
    print("Campos a editar: nombre, poblacion, superficie, continente")
    campo = input("Ingrese el campo que desea editar: ").strip().lower()

    #Si es igual al encabezado lo edita
    
    if campo == "nombre":
        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip().title()
            if not nuevo_nombre:
                print("El nombre no puede estar vacío.")
                continue
            if any(p["nombre"].lower() == nuevo_nombre.lower() and p != pais for p in paises):
                print("Ese nombre ya existe en el archivo.")
                continue
            pais["nombre"] = nuevo_nombre
            break
    elif campo == "poblacion":
        pais["poblacion"] = ingresar_entero("Ingrese la nueva población: ")
    elif campo == "superficie":
        pais["superficie"] = ingresar_entero("Ingrese la nueva superficie (km²): ")
    elif campo == "continente":
        pais["continente"] = ingresar_continente()
    else:
        print("Campo inválido.")
        return

    # Guardar todos los países nuevamente en el CSV
    with open(ARCHIVO, "w", encoding="utf-8", newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
        escritor.writeheader()
        escritor.writerows(paises)

    print("Actualizado.")
