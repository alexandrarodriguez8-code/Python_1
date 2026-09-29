#Variables
#Condicionales
#Ciclos
#Manejo de errores

#Empresa de bus. Vende tiquetes:

'''

Medellín -> Bogotá = 120.000
Medellín -> Cali = 100.000
Medellín -> Barranquilla = 150.000
Medellín -> Cartagena= 200.000

Proceso compra:
Solicitar:
Destino:
Cantidad de tiquetes:
Según la cantidad de tiquetes pedor los nombres de los pasajeros.
Calcular total a pagar.
Mostrar destino, los nombres de los pasajeros.
Calcular total a pagar.
Mostar destino, los nombres de los pasajeros y el total a pagar.

'''
#Ciclo infinito para que se repita todo el proceso

while True:
    print("=== Tiquete de bus ===\n")

    #Variable para preguntar al usuario: Opción

    try:
        menu =int(input("""
    
        Seleccion ruta a comprar:
        1. Medellín - Bogotá
        2. Medellín - Cali
        3. Medellín - Barranquilla
        4. Medellín - Cartagena
        5. Salir 
    
        """))

        #Condicional: Verificar que opción escogio la persona
        if menu in range (1,5):

            valor_tiquete = 0 
            if menu ==1:
                valor_tiquete =120000
                ruta ="Medellín - Bogotá"
            elif menu ==2:
                valor_tiquete =100000
                ruta ="Medellín - Cali"
            elif menu ==3:
                valor_tiquete =150000
                ruta ="Medellín - Barranquilla"
            else:
                valor_tiquete =200000
                rura ="Medellín - Cartagena"

            try:
                cantidad =int(input("Cantidad de tiquetes a comprar : "))
                lista_pasajeros =[]
                for i in range (cantidad):
                    pasajero =input(f"Ingrese el nombre del pasajero {i+1} ")
                    #Guardar el valor de la variable en la lista
                    lista_pasajeros.append(pasajero)

                #Mostrar todo
                print(f"""
                === RESUMEN DE COMPRA ===
                -Ruta = {ruta}
                -Cantidad pasajeros = {cantidad}
                -Valor tiquete = {valor_tiquete}
                -Total = {cantidad * valor_tiquete}
                -Pasajeros = {lista_pasajeros}
                """)    

            except ValueError:
                print("Ingrese una cantidad válida")

        elif menu ==5:
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida")
            break


    except ValueError:
        print("Ingrese una opción válida")

        