"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4 porciento de
 interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año,
  se te añaden al balance final de tu cuenta de ahorros. 
  Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta
   de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar 
   por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
    cada cantidad a dos decimales.



"""

cantidadDeposito=float(input("Ingrese la cantidad de dinero que desea depostitar: "))
interes = 0.04
primerAnio=cantidadDeposito*(1+interes)
segundoAnio=primerAnio*(1+interes)
tercerAnio=segundoAnio*(1+interes)

redondeoUno=round(primerAnio,2)
redondeoDos=round(segundoAnio,2)
redondeoTres=round(tercerAnio,2)

print("El ahorro del primer año es: ", redondeoUno)
print("El ahorro del segundo año es: ", redondeoDos)
print("El ahorro del tercer año es: ", redondeoTres)

