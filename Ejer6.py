# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:23:18 2024

@author: ddiaz
"""

import random

def generar_individuo(num_c):
    ind = list(range(num_c))
    random.shuffle(ind)
    return ind

def inicializar(tam_p, num_c):
    return [generar_individuo(num_c) for _ in range(tam_p)]

def calcular_distancia(ind, dist):
    distancia_t = 0
    for i in range(len(ind)):
        distancia_t += dist[ind[i]][ind[(i + 1) % len(ind)]]
    return distancia_t

def seleccion(poblacion, distancias, k=3):
    seleccionados = random.sample(poblacion, k)
    seleccionados.sort(key=lambda x: calcular_distancia(x, distancias))
    return seleccionados[0]

def crossover_orden(padre1, padre2):
    size = len(padre1)
    a, b = sorted(random.sample(range(size), 2))
    hijo1 = [None] * size
    hijo1[a:b] = padre1[a:b]
    p2 = [item for item in padre2 if item not in hijo1]
    i = 0
    for j in range(size):
        if hijo1[j] is None:
            hijo1[j] = p2[i]
            i += 1
    return hijo1

def mutacion(ind):
    a, b = random.sample(range(len(ind)), 2)
    ind[a], ind[b] = ind[b], ind[a]
    return ind

def algoritmo_g(distancias, tam_p=100, num_g=500, prob_cruce=0.8, prob_m=0.1):
    num_ciudades = len(distancias)
    poblacion = inicializar(tam_p, num_ciudades)
    
    for _ in range(num_g):
        nueva_poblacion = []
        
        for _ in range(tam_p // 2):
            padre1 = seleccion(poblacion, distancias)
            padre2 = seleccion(poblacion, distancias)
            
            if random.random() < prob_cruce:
                hijo1 = crossover_orden(padre1, padre2)
                hijo2 = crossover_orden(padre2, padre1)
            else:
                hijo1, hijo2 = padre1, padre2
            
            if random.random() < prob_m:
                hijo1 = mutacion(hijo1)
            if random.random() < prob_m:
                hijo2 = mutacion(hijo2)
            
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion
    
    mejor_ind = min(poblacion, key=lambda x: calcular_distancia(x, distancias))
    mejor_dist = calcular_distancia(mejor_ind, distancias)
    return mejor_ind, mejor_dist
distancias = [
    [0, 7, 9, 8, 20],
    [7, 0, 10, 4, 11],
    [9, 10, 0, 15, 5],
    [8, 4, 15, 0, 17],
    [20, 11, 5, 17, 0]
]

mejor_ruta, mejor_distancia = algoritmo_g(distancias)
print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia total:", mejor_distancia)



