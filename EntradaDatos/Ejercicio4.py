"""
Escribir un programa que pregunte el nombre del usuario y un numero entero n
y muestre el nombre la cantidad de veces n introducida
"""
n=int(input("Ingrese la cantidad de veces que desea que se repita el nombre: "))
for i in range(1,n+1):
    nombre=input("Introduce tu nombre:")
    print(nombre)