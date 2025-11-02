from utilidades import CONTINENTES_VALIDOS

# Validar entero
def ingresar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")

# Verificar que el rango máximo no sea menor al mínimo.
def ingresar_rango(mensaje_min, mensaje_max):
    while True:
        min_val = ingresar_entero(mensaje_min)
        max_val = ingresar_entero(mensaje_max)
        if min_val > max_val:
            print("El valor mínimo no puede ser mayor que el máximo. Intente nuevamente.")
        else:
            return min_val, max_val

# Verificar continente.
def ingresar_continente():
    while True:
        cont = input("Ingrese el continente: ").strip().title()
        if cont in CONTINENTES_VALIDOS:
            return cont
        else:
            # Con join se muestra la lista de continentes válidos separándolos con una coma y un espacio.
            print(f"Continente inválido. Debe ser uno de: {', '.join(CONTINENTES_VALIDOS)}")
