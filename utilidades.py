import csv
import os
import unicodedata  # Se importa para manejar acentos

# Se define el encabezado y los continentes que serán válidos para los continentes.
ARCHIVO = "paises.csv"
ENCABEZADO = ["nombre", "poblacion", "superficie", "continente"]
CONTINENTES_VALIDOS = ("América", "Asia", "Europa", "África", "Oceanía", "Antártida")

# Función para quitar acentos de los textos
def quitar_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Si el archivo paises.csv no existe se crea.
def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8", newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
            escritor.writeheader()
        print("Archivo creado correctamente con encabezado:", ENCABEZADO)

# Carga los países y verifica que no hayan habido cambios en el encabezado, o errores en el contenido.
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

# Muestra la lista completa de países del csv.
def mostrar_lista(lista):
    if not lista:
        print("No se encontraron resultados.")
    else:
        for p in lista:
            print(f"{p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")
