def calcular_suma(num1:int,num2:int)->int:
    '''
    Funcion que recibe dos numeros y se encarga de sumarlos
    '''
    resultado_suma = num1 + num2
    return resultado_suma

def calcular_resta(num1:int,num2:int)->int:
    '''
    Funcion que recibe dos numeros y se encarga de restarlos
    '''
    resultado_resta = num1 - num2
    return resultado_resta

def calcular_division(num1:int,num2:int)->float:
    '''
    Funcion que recibe dos numeros y se encarga de dividirlos en donde si uno de los numeros que recibe es cero,
    muestra un error ya que no se puede dividr por dicho numero.
    '''
    if num1 == 0:
        print("No se puede dividir por cero") 
    else: 
        resultado_division = num1 / num2
        return resultado_division

def calcular_multiplicacion(num1:int,num2:int)->int:
    '''
    Funcion que recibe dos numeros y se encarga de multiplicarlos
    '''
    resultado_multiplicacion = num1 * num2
    return resultado_multiplicacion 

def calcular_potencia(num1:int,num2:int)->int:
    '''
    Función que recibe dos números y se encarga de 
    calcular la potencia del primer número elevado 
    al segundo número.
    '''
    resultado_potencia = num1 ** num2
    return resultado_potencia

def calcular_resto(num1:int,num2:int)->int:
    '''
    Funcion que recibe dos numeros y se encarga de calcular el resto.
    si alguno de los numeros que recibe es cero, muestra un mensaje de error.
    '''
    if num1 == 0:
        print("No se puede dividir por cero")
    else:
        resultado_resto = num1 % num2
        return resultado_resto

def calcular_factorial_n1(num1:int)->int:
    '''
    funcion que recibe un numero (primer operando) y se encarga de calcular el factorial utilizando bucle for.
    '''
    fact = 1
    for i in range(1,num1+1):
        fact*= i
    return fact
def calcular_factorial_n2(num2:int)->int:
    '''
    funcion que recibe un numero (segundo operando) y se encarga de calcular el factorial utilizando el concepto de recursividad
    '''
    if num2 == 0:
        return 1
    else:
        return num2 * calcular_factorial_n2(num2-1)