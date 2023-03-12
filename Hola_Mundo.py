import numpy as np
import matplotlib.pyplot as plt

# Definición de funciones

# Gracias ChatGPT por la magia negra y por ser mi compa
def markov_simulation(P, n, init_state):
    states = [init_state]
    for i in range(n-1):
        next_state = np.random.choice([0, 1, 2], p=P[states[-1]])
        states.append(next_state)
    return states.pop(1)

# Definición de constantes

dictTraductorTipos = {0:"A", 1:"S", 2:"R"}
proporciones = [0.75, 0.2, 0.05] #(A,S,R) = (0,1,2) Proporciones de población
matrizTransicion = [[0, 0.3, 0.7], [0.1, 0.4, 0.5], [0.4, 0.4, 0.2]]

# Captura N (Tamaño de población total)

print("Dame una N grande :)")
N = int(input())

# Captura t (Tiempo de simulación)

print("Dame un tiempo discreto")
t = int(input())

#---

MN =[list(map(lambda x: int(x*N), proporciones))]
print(MN)

#---
#Pruebas de simulación

# count = 0
# for j in range(3):
#     for i in range(int(N * MN_t0[j])):
#         count += 1
#         print(count, "Tipo:", translatedict[j], "-->", translatedict[markov_simulation(Matriz, 2, j)])

#---
