from utilidades import cargar_paises

# Muestra estadísticas generales.
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

# Muestra los países por continente con un contador.
def cantidad_por_continente():
    paises = cargar_paises()
    conteo = {}
    for p in paises:
        cont = p["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1
    for cont, cantidad in conteo.items():
        print(f"{cont}: {cantidad} países")
