import numpy as np
import time

def ordenacao(vetor):
    ti = time.time()
    n = len(vetor)
    for i in range(n):
        menor_valor = i 
        for j in range(i + 1, n):
            if vetor[j] < vetor[menor_valor]:  
                menor_valor = j
        vetor[i], vetor[menor_valor] = vetor[menor_valor], vetor[i] 
    print(vetor)
    duracao = time.time() - ti
    return duracao


vetor = np.array([])
print(ordenacao(vetor))

