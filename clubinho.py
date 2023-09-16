lista = list()

for i in range(4):
    lista.append(int(input()))

if lista[0] + lista[1] + lista[2] == lista[3]:
    valor = 0
    flag = True
    for i in lista:
        if valor < i:
            valor = i
        else: 
            flag = False
            print("NEGADO")
            break
    if flag:
        print("LIBERADO")
    
    

else:
    print("NEGADO")
   
        