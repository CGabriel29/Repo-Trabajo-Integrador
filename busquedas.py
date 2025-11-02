from utilidades import cargar_paises, quitar_acentos, mostrar_lista

# Carga la lista de países y si coincide el nombre ingresado por el usuario muestra sus características.
def buscar_pais(nombre):
    paises = cargar_paises()
    nombre_normalizado = quitar_acentos(nombre.lower())
    resultados = [p for p in paises if nombre_normalizado in quitar_acentos(p["nombre"].lower())]
    mostrar_lista(resultados)
