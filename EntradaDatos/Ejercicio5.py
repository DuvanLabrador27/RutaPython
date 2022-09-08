"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
nombre=input("Introduce tu nombre:")
nHoras=int(input("Introduce el número de horas trabajadas: "))
costoHora=float(input("Introduce el costo por hora: "))
pago=nHoras*costoHora
print(f"Hola {nombre}, las horas de trabajo son {nHoras} y el pago por sus horas trabajadas es de {pago}")

