import numpy as np

def ordenacao(vetor):
    n = len(vetor[0])
    for i in range(n):
        menor_valor = i 
        for j in range(i + 1, n):
            if vetor[0, j] < vetor[0, menor_valor]:
                menor_valor = j
        vetor[0, i], vetor[0, menor_valor] = vetor[0, menor_valor], vetor[0, i]
    print(' '.join(map(str, vetor[0].astype(int))))

n = int(input())
vetor = np.zeros((1, n))
cont = input()
num = 0
for i in cont.split():
    vetor[0, num] = int(i)
    num = num + 1

ordenacao(vetor)
