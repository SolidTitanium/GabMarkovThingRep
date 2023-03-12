import numpy as np
import matplotlib.pyplot as plt

# Definición de funciones y otros

# Gracias ChatGPT por la magia negra y por ser mi compa
def markov_simulation(P, n, init_state):
    states = [init_state]
    for i in range(n-1):
        next_state = np.random.choice([0, 1, 2], p=P[states[-1]])
        states.append(next_state) 
    return states.pop(1)

def agregarPoblacion(tipo, MNBuff):
    MNBuff[tipo] += 1
    return MNBuff

def construirMN(MNBuff, MN):
    MN.append(MNBuff)
    return MN

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

# Decalración de variables

t_actual = 1
MN = [list(map(lambda x: int(x*N), proporciones))]
MNBuff = [0, 0, 0]

# Ciclo de simulación

while t_actual <= t:
    for j in range(3):
        for i in range(MN[t_actual - 1][j]):
            MNBuff = agregarPoblacion(markov_simulation(matrizTransicion, 2, j), MNBuff)
    MN = construirMN(MNBuff, MN)
    MNBuff = [0, 0, 0]
    t_actual += 1

# Impresión de resultados

for index, tiempo in enumerate(MN):
    print("tiempo:", index, "Historia:", tiempo)