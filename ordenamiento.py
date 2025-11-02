from utilidades import cargar_paises, mostrar_lista

# Ordena los países según la clave seleccionada.
def ordenar_paises(clave, descendente=False):
    paises = cargar_paises()
    ordenados = sorted(paises, key=lambda x: x[clave], reverse=descendente)
    mostrar_lista(ordenados)
