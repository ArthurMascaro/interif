S = input().lower()

vogais = ['a', 'e', 'i', 'o', 'u']

cont = 0 

for letra in S:
    if letra in vogais:
        cont+=1
resto = cont % 3
if resto == 1:
    print("frasco 1")
elif resto == 2:
    print("frasco 2")
else:
    print("frasco 0")