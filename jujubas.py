import math
P = str(input().strip().replace(" ", ""))
N = int(input())
T = list()

compare = list()

def distance(string1, string2):
    if (len(string1) != len(string2)):
        raise ValueError("Strings lentchs must match")
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            count+=1
    return count

for i in range(N):
    jujubas = str(input().strip().replace(" ", ""))
    T.append(jujubas)

for pack in T:
    compare.append(distance(P, pack))

def rule(value, total):
    return (100 * value) / total

for i in range(len(compare)):
    compare[i] = len(P) - compare[i]

percent = []
M = int(input())
for i in range(M):
    percent.append(int(input()))

difpercent = list()
success = list()

for c in compare:
    difpercent.append(rule(c, len(P)))

def rule_success(passou, total):
    return (100 * passou) / total

for p in percent:
    count = 0
    for d in difpercent:
        if d >= p:
            count += 1
    success.append(rule_success(count, N))

for s in success:
    if str(s).split('.')[1] == '0':
        print(str(s).split('.')[0] + '.00')
    else:
        print(round(float(s), 2))
    
