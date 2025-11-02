import csv
from utilidades import cargar_paises, ARCHIVO, ENCABEZADO
from validaciones import ingresar_entero, ingresar_continente

# Agrega un país con todas sus características.
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

# Edita la característica seleccionada de un país.
def editar_pais():
    paises = cargar_paises()
    if not paises:
        print("No hay países en el archivo para editar.")
        return

    from utilidades import mostrar_lista
    mostrar_lista(paises)
    
    nombre_buscar = input("Ingrese el nombre del país a editar: ").strip().lower()
    coincidencias = [p for p in paises if nombre_buscar in p["nombre"].lower()]

    if not coincidencias:
        print("No se encontró ningún país con ese nombre.")
        return

    pais = coincidencias[0]

    print("Campos a editar: nombre, poblacion, superficie, continente")
    campo = input("Ingrese el campo que desea editar: ").strip().lower()

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

    with open(ARCHIVO, "w", encoding="utf-8", newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
        escritor.writeheader()
        escritor.writerows(paises)

    print("Actualizado.")
