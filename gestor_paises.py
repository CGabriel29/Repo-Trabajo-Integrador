import csv
import os

ARCHIVO = "paises.csv"
ENCABEZADO = ["nombre", "poblacion", "superficie", "continente"]

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

def buscar_pais(nombre):
#Recibe un string 'nombre' para buscar coincidencias parciales o exactas en los nombres de países.
#Devuelve una lista de países que coinciden y la muestra por consola.
    
    paises = cargar_paises()
    resultados = [p for p in paises if nombre.lower() in p["nombre"].lower()]
    mostrar_lista(resultados)

def filtrar_por_continente(cont):
    #Recibe un string 'cont' que representa el nombre de un continente.
    #Filtra los países que pertenecen a ese continente y los muestra por consola.
    paises = cargar_paises()
    filtrados = [p for p in paises if p["continente"].lower() == cont.lower()]
    mostrar_lista(filtrados)

def filtrar_por_poblacion(min_pob, max_pob):
    #Recibe dos enteros: 'min_pob' y 'max_pob' como límites del rango de población.
    #Devuelve los países cuya población está dentro del rango especificado.

    paises = cargar_paises()
    filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
    mostrar_lista(filtrados)

def filtrar_por_superficie(min_sup, max_sup):
    #Recibe dos enteros: 'min_sup' y 'max_sup' como límites del rango de superficie.
    #Devuelve los países cuya superficie está dentro del rango especificado.
    paises = cargar_paises()
    filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
    mostrar_lista(filtrados)

def ordenar_paises(clave, descendente=False):
    #Recibe un string 'clave' que indica el campo por el cual ordenar ('nombre', 'poblacion', 'superficie'),
    #y un booleano 'descendente' que indica si el orden debe ser descendente.
    #Devuelve la lista ordenada y la muestra por consola.
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

def agregar_pais():
    #Agrega un país al CSV
    pais = {}
    pais["nombre"] = input("Ingrese el nombre del país: ").strip()
    pais["nombre"] = pais["nombre"].title()

    #Cargar países existentes para verificar si hay duplicados.
    paises = cargar_paises()
    if any(p["nombre"].lower() == pais["nombre"].lower() for p in paises):
        print(f"{pais["nombre"]} ya existe en el archivo.")
        return

    try:
        pais["poblacion"] = int(input("Ingrese la población: "))
        pais["superficie"] = int(input("Ingrese la superficie (km²): "))
    except ValueError:
        print("Error: población y superficie deben ser números enteros.")
        return

    pais["continente"] = input("Ingrese el continente: ").strip()
    pais["continente"] = pais["continente"].title()
    
    #Guardar país
    with open(ARCHIVO, "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
        escritor.writerow(pais)
    print(f"{pais['nombre']} agregado.")

def mostrar_lista(lista):
    #Recibe una lista de países (diccionarios).
    #Si la lista está vacía, muestra un mensaje. Si tiene elementos, los imprime en formato legible.
    if not lista:
        print("No se encontraron resultados.")
    else:
        for p in lista:
            print(f"{p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")

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
        print("11. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
            print("-----------------------------------")

            match opcion:
                case 1:
                    nombre = input("Ingrese nombre o parte del nombre: ")
                    buscar_pais(nombre)
                case 2:
                    cont = input("Ingrese continente: ")
                    filtrar_por_continente(cont)
                case 3:
                    min_p = int(input("Población mínima: "))
                    max_p = int(input("Población máxima: "))
                    filtrar_por_poblacion(min_p, max_p)
                case 4:
                    min_s = int(input("Superficie mínima: "))
                    max_s = int(input("Superficie máxima: "))
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
                    print("Gracias por usar el sistema.")
                    break
                case _:
                    print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número válido.")

if __name__ == "__main__":
    inicializar_archivo()
    menu()
