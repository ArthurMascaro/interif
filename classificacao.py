import re

pilotos = dict()
voltas = dict()
voltasAN = []

a, b, c = [int(i) for i in input().split(' ')]

for i in range(a):
    nome = input()
    sigla = nome[:3]
    sigla = sigla.upper()
    pilotos[sigla] = nome


for i in range(b):
    nome, tempo = input().split(' ')
    if nome not in voltas.keys():
         voltas[nome] = [[i+1, tempo]]
    else:
        voltas[nome].append([i+1, tempo])

for i in range(c):
    nome, tempo = input().split(' ')
    lista = voltas[nome]
    for j in range(len(lista)):
        if lista[j][1] == tempo:
            lista.pop(j)
            voltas[nome] = lista
            break

for i in voltas.keys():
    lista = voltas[i]
    for j in range(len(lista)):
        voltasAN.append(lista[j])

def natural_sort(lista):
    def alphanum_key(key):
        return [int(s) if s.isdigit() else s.lower() for s in re.split("([0-9]+)", key)]
    return sorted(lista, key=alphanum_key)

tempos = list()
for i in range(len(voltasAN)):
    tempos.append(voltasAN[i][1])
tempos = natural_sort(tempos)

final =(a+1) * [None]

for p in voltas.keys():
    piloto = pilotos[p]
    temposP = list()
    for k in voltas[p]:
        temposP.append(k[1])
    for j in voltas[p]:
        volta = j[0]
        melhor = natural_sort(temposP)[0]
        pos = tempos.index(melhor)
        tempos[pos] = None
        classificado = {"nome": piloto, "volta": volta, "tempo": melhor}
        final[pos] = classificado
        break

q = final.count(None)
for i in range(q):
    final.remove(None)

for i in range(len(final)):
    if i+1 != len(final):
        if final[i]["tempo"] == final[i+1]["tempo"]:
            t1 = final[i]["volta"]
            t2 = final[i+1]["volta"]
            if t2 < t1:
                antes = final[i]
                depois = final[i+1]
                final[i] = depois
                final[i+1] = antes

for i in range(len(final)):
    print(str(i+1)+ ' '+final[i]["nome"].strip()+ ' '+final[i]["tempo"])
            





        