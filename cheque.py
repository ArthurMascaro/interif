import math


N = int(input())
fvalues = list()

for i in range(N):
    F = int(input())
    fvalues.append(F)

fvalues = sorted(fvalues)
fvalues_copy = fvalues.copy()
V = int(input())

nC = 0

for f in fvalues:
    cont = 0
    max_f = max(fvalues_copy)
    cont = math.floor(V/max_f)
    nC += cont
    V -= cont * max_f
    fvalues_copy.remove(max_f)

print(nC)