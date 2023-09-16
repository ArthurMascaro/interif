E = int(input())
N = int(input())

partidas = list()
time = dict()
equipeA = ""
equipeB = ""
placar = ""
vpontos = 0
vvitorias = 0
vsg = 0



placares = list()

for i in range(N):
    jogo = [str(i) for i in input().split()]
    partidas.append(jogo)

for partida in partidas:
    equipeA = partida[0]
    equipeB = partida[4]

    time[equipeA] = [0] * 3
    time[equipeB] = [0] * 3

    resultado = dict()
    resultado[equipeA] = int(partida[1])
    resultado[equipeB] = int(partida[3])
    placares.append(resultado)

    for p in placares:
        if p.get(equipeA) > p.get(equipeB):
            time[equipeA][0] += 3
            time[equipeA][1] += 1
            time[equipeA][2] += p.get(equipeA)

            time[equipeB][2] = p.get(equipeA) - p.get(equipeB)
        elif p.get(equipeA) < p.get(equipeB):
            time[equipeB][0] += 3
            time[equipeB][1] += 1
            time[equipeB][2] += p.get(equipeB)

            time[equipeA][2] = p.get(equipeA) - p.get(equipeB)
        else:
            time[equipeA][0] += 1
            time[equipeB][0] += 1

for t in time.keys():
    print(t + ' '+ str(time[t][0])+' '+str(time[t][1])+' '+str(time[t][2]))

        



    
