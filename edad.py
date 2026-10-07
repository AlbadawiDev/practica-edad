"""Ejercicio de condición con umbral fijo de 18 años."""


def es_mayor(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    return edad >= 18


def main():
    try:
        edad = int(input("¿Cuántos años tienes? "))
        print("Eres mayor de edad." if es_mayor(edad) else "No eres mayor de edad.")
    except (ValueError, EOFError):
        print("Entrada inválida: ingrese una edad entera cero o positiva.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
