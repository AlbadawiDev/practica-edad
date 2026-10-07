# Practica Edad

Este repositorio contiene el script **edad.py**, que:

- Pide al usuario su edad en años.
- Comprueba si es mayor de edad (≥18) o no.
- Muestra un mensaje en función de la edad ingresada.

**Uso**:
```bash
python edad.py

```

## Verificación local

Ejercicio de aprendizaje con funciones importables, validación de entrada y pruebas sin dependencias externas.

```powershell
python -X utf8 edad.py
python -X utf8 -m unittest discover -v
```

La entrada inválida devuelve código de salida 1 sin traceback. Las pruebas verifican límites y la consola.
