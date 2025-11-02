from utilidades import cargar_paises, mostrar_lista

# Muestra la lista de países según el continente.
def filtrar_por_continente(cont):
    paises = cargar_paises()
    filtrados = [p for p in paises if p["continente"].lower() == cont.lower()]
    mostrar_lista(filtrados)

# Muestra según un rango mínimo y máximo de población.
def filtrar_por_poblacion(min_pob, max_pob):
    paises = cargar_paises()
    filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
    mostrar_lista(filtrados)

# Muestra según un rango mínimo y máximo de superficie.
def filtrar_por_superficie(min_sup, max_sup):
    paises = cargar_paises()
    filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
    mostrar_lista(filtrados)
