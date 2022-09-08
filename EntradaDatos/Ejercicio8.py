"""
Escribir un programa que pida al usuario dos números enteros y muestre 
por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto
 de la división entera respectivamente.
"""

n1=int(input("Introduce un numero entero: "))
n2=int(input("Introduce otro numero entero: "))
c=n1/n2
r=n1%n2
print("El cociente de la división es: ",c)
print("El resto de la división es: ",r)