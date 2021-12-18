import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
# import the graph in dictionary key : Neighborhood of key
cycle = int(input("The number of vertices in cycle "))


number_of_iteration = 100000
Time_taken = []
for i in range(number_of_iteration):
# Initial position of cop and robber
    j = 0
    cop = 0
    robber = random.choice(range(2 * cycle))
    print("Initial position of cop is ", cop)
    print("Initial position of robber is ", robber)
    # Game play
    while j >= 0:
        if cop == robber :
            #print("Robber go to cop")
            break
        j += 1
# Cop strategies
        minus = abs((cop - robber % cycle) % cycle)
        add = abs((robber % cycle - cop) % cycle)
        print('add', add, 'minus', minus)
        if cycle % 4 == 3 and robber == ((cop + (cycle-1)/2) % (cycle) + cycle) % (2*cycle): cop = (cop - 1) % cycle
        elif cycle % 4 == 3 and robber == ((cop + (cycle+1)/2) % (cycle) + cycle) % (2*cycle) : cop = (cop + 1) % cycle
        elif (cop == (robber + 1) % cycle and robber < cycle) or (cop == (robber - 1) % cycle and robber < cycle) or cop == robber % cycle:
            cop = robber
        elif add <= minus:
            cop = (cop + 1) % cycle
        else : cop = (cop - 1) % cycle

        print("position of cop in turn {} is ".format(j), cop)
        if cop == robber :
            #print("Cop catch the robber")
            break
    #Robber move
        if robber >= cycle: robber = random.choice([(robber + 1) % cycle + cycle, (robber -1) % cycle + cycle, robber - cycle])
        else: robber = random.choice([(robber + 1) % cycle , (robber -1) % cycle , robber + cycle])
        print("position of robber in turn {} is ".format(j), robber)
    print('The time taken until the game end ', j)
    Time_taken.append(j)
    print('######################################################')
Expected_capture_time = statistics.mean(Time_taken)
print("The expected capture time of a graph G is ", Expected_capture_time)
print("The Standard Error is ", sem(Time_taken))
l = [i for i in np.arange(0, max(ele for ele in Time_taken), 1)]
plt.style.use('ggplot')
plt.hist(Time_taken, bins=l)
plt.show()