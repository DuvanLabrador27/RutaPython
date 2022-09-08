
lista = []
balanceados = True
i = 0
n=int(input())

for cant in range(n):
    cadena =input("")
    while i < len(cadena) and balanceados:
        simbolo = cadena[i]
        if simbolo == "(":
            lista.append(simbolo)
        else:
            if len(lista)==0:
                balanceados = False
            else:
                lista.pop()
        


        i = i + 1

if balanceados and len(lista)==0:
    print("CORRECTO")
else:
    print("INCORRECTO")


    


            

   



