
cont=0
cont2=0
cont3=0
presidentes=[]
votos=[]

n=int(input("Cantidad de presidentes: "))

for j in range(1,n+1):
    nombrePresidente=input("Ingrese el nombre del presidente: ")
    ciudad=int(input("Ingrese la cantidad de ciudades: "))
    
    for k in range(1,ciudad+1):
        cantidadVotos=int(input("Ingrese la cantidad de votos por ciudades: "))
           
    if nombrePresidente=="Petro":
        presidentes.append(nombrePresidente)
        votos.append(cantidadVotos)
        cont=cont+cantidadVotos
        
    elif  nombrePresidente=="Duque":
        presidentes.append(nombrePresidente)
        votos.append(cantidadVotos)
        cont2=cont2+cantidadVotos
    
    elif  nombrePresidente=="PastorTrujillo":
        presidentes.append(nombrePresidente)
        votos.append(cantidadVotos)
        cont3=cont3+cantidadVotos
    for v in votos:
        print(v)
    

print(presidentes)
print(votos)
print(cont)
print(cont2)
print(cont3)
    

