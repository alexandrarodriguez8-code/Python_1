"""
try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado: {numero}")

except ValueError:
    print("Error: Por favor, ingrese un número válido.")
"""

menu =0

while menu != 3: 
    try:
        menu = int(input("""Ingrese una opción: 
        n1. Sumar
        n2. Restar
        n3. Salir
        """))
    
        if menu == 1:
            n1=int(input("Ingrese el primer número:"))
            n2=int(input("Ingrese segundo número: "))
            print(f"Resultado {n1+n2}")

        elif menu == 2:
                n1=int(input("Ingrese el primer número:"))
                n2=int(input("Ingrese segundo número: "))
                print(f"Resultado {n1-n2}")

        else:
         print("Opción válida")

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

print("Saliendo del sistema")

# Ejercicio 1: try / except básico
try:
    numero = int(input("Ingrese un númeroentero: "))
    print(f"El número ingresado es: {numero}")

except ValueError:
    print("Error: Debe ingresar un número entro válido.")

# Ejercicio 2: División segura con ZeroDivisionError
try:
    dividiendo = float(input("Ingrese el dividiendo: "))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividiendo/divisor
    print(f"Resultado: {dividiendo} / { divisor} = {resultado}")

except ZeroDivisionError:
    print("Error: Ingrese únicamentevalores numéricos.")

# Ejercicio 3: else y finally

try: 
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: La eddad debe ser un número entero.")
else:
    if edad >= 18: 
        print("Acceso permitido.")
    else:
        print("Acceso denegado: Debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")

# Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente

while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break   
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

# Ejercicio 5: raise — lanzar una excepción personalizada

def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")