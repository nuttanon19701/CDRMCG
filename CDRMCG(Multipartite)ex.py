import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
from itertools import islice

# Input the number of vertices in each multipartite
Input = input("The number of vertices in each partite (ex. 1,2,2 ) ")
No_Partite = list(int(x) for x in Input.split(","))
print(No_Partite)
total_vertex = sum(list(No_Partite))
total_partite = len(No_Partite)
Set_of_vertex = list(range(total_vertex))
it_Set_of_vertex = iter(Set_of_vertex)
Set_of_partite = list(map(chr, range(ord('A'), ord('A')+total_partite)))
Set_of_vertex2 = [set(islice(it_Set_of_vertex, elem))
          for elem in No_Partite]
Vertex_in_partite = {}
for i in range(total_partite):
    Vertex_in_partite[Set_of_partite[i]] = Set_of_vertex2[i]
print(Vertex_in_partite)

graph = {}
for partite in Vertex_in_partite:
    for elem in Vertex_in_partite[partite]:
        O = set(Set_of_vertex)
        graph[elem] = O - Vertex_in_partite[partite]
print(graph)

number_of_iteration = 100000
Time_taken = []
for i in range(number_of_iteration):
# Initial position of cop and robber
    i = 0
    cop = random.choice(list(Vertex_in_partite['A']))
    p_cop = 'A'
    vertex = list(graph.keys())
    robber = random.choice(vertex)
    print("Initial position of cop is ", cop)
    print("Initial position of robber is ", robber)
    # Game play
    while i >= 0:
        if cop == robber :
            print("Robber go to cop")
            break
        i += 1
# Cop strategies
        if p_cop == 'A':
            p_cop = 'B'
        else : p_cop = 'A'
        if robber in graph[cop]:
            cop = robber
        else :
            cop = random.choice(list(Vertex_in_partite[p_cop]))
        print("position of cop in turn {} is ".format(i), cop)
        if cop == robber :
            print("Cop catch the robber")
            break
#Robber move
        Neighborhood_Robber = list(graph[robber])
        robber = random.choice(Neighborhood_Robber)
        print("position of robber in turn {} is ".format(i), robber)
    print('The time taken until the game end ', i)
    Time_taken.append(i)
    print('######################################################')
Expected_capture_time = statistics.mean(Time_taken)
print("The expected capture time of a graph G is ", Expected_capture_time)
print("The Standard Error is ", sem(Time_taken))
l = [i for i in np.arange(0, max(ele for ele in Time_taken), 1)]
plt.style.use('ggplot')
plt.hist(Time_taken, bins=l)
plt.show()