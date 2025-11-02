from validaciones import ingresar_entero, ingresar_rango, ingresar_continente
from utilidades import inicializar_archivo
from busquedas import buscar_pais
from filtros import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamiento import ordenar_paises
from estadisticas import estadisticas, cantidad_por_continente
from gestion import agregar_pais, editar_pais


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
