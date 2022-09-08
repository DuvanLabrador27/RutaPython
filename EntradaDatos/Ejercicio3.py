"""
Escribir un programa que pregunte el nombre del usuario en la consola y despues de que
el usuario lo introduzca muestre por pantalla la cadena <nombre> tiene n letras, donde 
nombre es el nombre de usuario en mayusuculas y n es la cantidad de letras que tienen.
"""

nombre=input("Introduce tu nombre: ")
print(f"{nombre} tiene {len(nombre)} letras")