"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número 
de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo
y la extensión.
"""

prefijo= input("Ingrese el prefijo: ")
numero=input("Ingrese el numero: ")
ext=input("Ingrese la extencion: ")

print(f"El numero sin el prefijo {prefijo} y la extencion {ext} es {numero}")

tel=input("Ingrese un numero con el forato +xx-xxxxxxxxx-xx:")
print(f"El numero es {tel[4:-3]}")