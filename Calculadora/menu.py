import os
from funciones import *

def menu():
    numero_1 = None
    numero_2 = None
    bandera = False
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            numero_1 = int(input("Ingrese Primer Operando: "))
        elif opcion == 2:
            numero_2 = int(input("Ingrese Segundo Operando: "))
        elif opcion == 3:
            if numero_1 == None or numero_2 == None:
                print("Error, ingrese los dos operandos")
            else:
                suma = calcular_suma(numero_1,numero_2)
                resta = calcular_resta(numero_1,numero_2)
                division = calcular_division(numero_1,numero_2)
                multiplicacion = calcular_multiplicacion(numero_1,numero_2)
                potencia = calcular_potencia(numero_1,numero_2)
                resto = calcular_resto(numero_1,numero_2)
                factorial_n1 = calcular_factorial_n1(numero_1)
                factorial_n2 = calcular_factorial_n2(numero_2)
                bandera = True
        elif opcion == 4:
            if bandera == False:
                print("Error, seleccione opcion la opcion 3 primero para calcular las operaciones")
            else:
                print(f"El resultado de {numero_1} + {numero_2} es de: {suma}")
                print(f"El resultado de {numero_1} - {numero_2} es de: {resta}")
                print(f"El resultado de {numero_1} / {numero_2} es de: {division}")
                print(f"El resultado de {numero_1} * {numero_2} es de: {multiplicacion}")
                print(f"{numero_1} elevado a la {numero_2} da como resultado: {potencia}")
                print(f"El resultado de {numero_1} % {numero_2} es de: {resto}")
                print(f"El factorial de {numero_1} es: {factorial_n1} y El factorial de {numero_2} es: {factorial_n2}")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('cls')
menu()
