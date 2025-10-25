import csv
import os

ARCHIVO = "paises.csv"
ENCABEZADO = ["nombre", "poblacion", "superficie", "continente"]
CONTINENTES_VALIDOS = ["América", "Asia", "Europa", "África", "Oceanía", "Antártida"]

def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8", newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
            escritor.writeheader()
        print("Archivo creado correctamente con encabezado:", ENCABEZADO)

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

def mostrar_lista(lista):
    if not lista:
        print("No se encontraron resultados.")
    else:
        for p in lista:
            print(f"{p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")

def buscar_pais(nombre):
    paises = cargar_paises()
    resultados = [p for p in paises if nombre.lower() in p["nombre"].lower()]
    mostrar_lista(resultados)

def filtrar_por_continente(cont):
    paises = cargar_paises()
    filtrados = [p for p in paises if p["continente"].lower() == cont.lower()]
    mostrar_lista(filtrados)

def filtrar_por_poblacion(min_pob, max_pob):
    paises = cargar_paises()
    filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
    mostrar_lista(filtrados)

def filtrar_por_superficie(min_sup, max_sup):
    paises = cargar_paises()
    filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
    mostrar_lista(filtrados)

def ordenar_paises(clave, descendente=False):
    paises = cargar_paises()
    ordenados = sorted(paises, key=lambda x: x[clave], reverse=descendente)
    mostrar_lista(ordenados)

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

def cantidad_por_continente():
    paises = cargar_paises()
    conteo = {}
    for p in paises:
        cont = p["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1
    for cont, cantidad in conteo.items():
        print(f"{cont}: {cantidad} países")

def ingresar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")

def ingresar_rango(mensaje_min, mensaje_max):
    while True:
        min_val = ingresar_entero(mensaje_min)
        max_val = ingresar_entero(mensaje_max)
        if min_val > max_val:
            print("El valor mínimo no puede ser mayor que el máximo. Intente nuevamente.")
        else:
            return min_val, max_val

def ingresar_continente():
    while True:
        cont = input("Ingrese el continente: ").strip().title()
        if cont in CONTINENTES_VALIDOS:
            return cont
        else:
            print(f"Continente inválido. Debe ser uno de: {', '.join(CONTINENTES_VALIDOS)}")

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


def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar país por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por rango de población")
        print("4. Filtrar por rango de superficie")
        print("5. Ordenar por nombre")
        print("6. Ordenar por población")
        print("7. Ordenar por superficie")
        print("8. Mostrar estadísticas")
        print("9. Cantidad de países por continente")
        print("10. Agregar nuevo país")
        print("11. Editar país")
        print("12. Salir")

        opcion = ingresar_entero("Ingrese una opción: ")
        print("-----------------------------------")

        match opcion:
            case 1:
                nombre = input("Ingrese nombre o parte del nombre: ")
                buscar_pais(nombre)
            case 2:
                cont = ingresar_continente()
                filtrar_por_continente(cont)
            case 3:
                min_p, max_p = ingresar_rango("Población mínima: ", "Población máxima: ")
                filtrar_por_poblacion(min_p, max_p)
            case 4:
                min_s, max_s = ingresar_rango("Superficie mínima: ", "Superficie máxima: ")
                filtrar_por_superficie(min_s, max_s)
            case 5:
                ordenar_paises("nombre")
            case 6:
                ordenar_paises("poblacion", descendente=True)
            case 7:
                ordenar_paises("superficie", descendente=True)
            case 8:
                estadisticas()
            case 9:
                cantidad_por_continente()
            case 10:
                agregar_pais()
            case 11:
                editar_pais()
            case 12:
                print("Gracias por usar el sistema.")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    inicializar_archivo()
    menu()
