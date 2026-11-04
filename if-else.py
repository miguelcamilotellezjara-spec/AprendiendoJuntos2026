"""
============================================================
- Descripción: Script que determina si una persona es mayor de edad.
- Entrada: Una variable numérica entera que representa la edad.
- Salida: Un mensaje por consola indicando si es mayor o menor de edad.
- Condición (if/else): Si la edad es mayor o igual a 18.
============================================================
"""
  """
============================================================
Miniespecificación (Estilo Guía Didáctica - UTPL):
1. Inicio
2. // Declaración de variables
3. edad, i[0-n] // Variable numérica entera que representa la edad
4. 
5. // Inicialización o asignación de entrada
6. edad <- 20
7. 
8. // Estructura de decisión doble
9. Si edad >= 18 entonces
10.     Escribir "La persona es mayor de edad."
11. De lo contrario
12.     Escribir "La persona es menor de edad."
13. Fin Si
14. Fin
============================================================
"""

# Definición de la variable de entrada
edad = 20

# Bloque básico if/else en Python
if edad >= 18:
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")