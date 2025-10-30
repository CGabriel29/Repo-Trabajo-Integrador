import runpy

# Carga todas las funciones del otro archivo sin crear pycache
funcs = runpy.run_path("funciones_paises.py")

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

        opcion = funcs["ingresar_entero"]("Ingrese una opción: ")
        print("-----------------------------------")

        match opcion:
            case 1:
                nombre = input("Ingrese nombre o parte del nombre: ")
                funcs["buscar_pais"](nombre)
            case 2:
                cont = funcs["ingresar_continente"]()
                funcs["filtrar_por_continente"](cont)
            case 3:
                min_p, max_p = funcs["ingresar_rango"]("Población mínima: ", "Población máxima: ")
                funcs["filtrar_por_poblacion"](min_p, max_p)
            case 4:
                min_s, max_s = funcs["ingresar_rango"]("Superficie mínima: ", "Superficie máxima: ")
                funcs["filtrar_por_superficie"](min_s, max_s)
            case 5:
                funcs["ordenar_paises"]("nombre")
            case 6:
                funcs["ordenar_paises"]("poblacion", descendente=True)
            case 7:
                funcs["ordenar_paises"]("superficie", descendente=True)
            case 8:
                funcs["estadisticas"]()
            case 9:
                funcs["cantidad_por_continente"]()
            case 10:
                funcs["agregar_pais"]()
            case 11:
                funcs["editar_pais"]()
            case 12:
                print("Gracias por usar el sistema.")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    funcs["inicializar_archivo"]()
    menu()
