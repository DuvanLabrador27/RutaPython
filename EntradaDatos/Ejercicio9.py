"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.
"""
import math
cantidadInvertir = float(input("Introduce la cantidad a invertir: "))
interesAnual = float(input("Introduce el interés anual: "))
numeroAnios = int(input("Introduce el número de años: "))
capital = cantidadInvertir * (1 + interesAnual / 100) 
capital= math.pow(capital,numeroAnios)
print("El capital obtenido en la inversión es: ", capital)
