'''
Centro de Biotecnologia Agropecuaria
Ficha: 2877795
Aprendiz: Julian Daniel Camacho Aguilar
version: 3.12.2
fecha: 25/04/2024
'''

#generando numero aleatorios del 0 al 100 con la libreria "random"

import random
n1 = random.randint(0,101)
n2 = random.randint(0,101)

print("los numeros generados son:", n1, n2)


# aqui se utiliza un F str para que imprima cualquier nombre

def saludo(nombre):
    print(f"hola {nombre}, todo bien?")

def suma(valor1, valor2):
    return valor1 + valor2

def resta(valor1,valor2):
    return valor1 - valor2

def multiplicacion(valor1,valor2):
    return valor1 * valor2

def division(valor1,valor2):
    if valor2 != 0:           #utilizo un condicional para que aparezca un mensaje si el divisor es 0
        return valor1 / valor2
    else:
        return "no se puede dividir entre 0"        

#aqui se llaman los resultados

saludo("julian")
print("la suma de los numeros anteriores es: ", suma(n1,n2))
print("la resta de los numeros anteriores es: ", resta(n1,n2))
print("la multiplicacion de los numeros anteriores es: ", multiplicacion(n1,n2))
print("la divison de los numeros anteriores es: ", division(n1,n2))





