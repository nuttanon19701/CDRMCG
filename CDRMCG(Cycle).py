import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
from itertools import islice

# Input the number of vertices in each multipartite
cycle = int(input("The number of vertices in cycle "))

number_of_iteration = 100000
Time_taken = []
for i in range(number_of_iteration):
# Initial position of cop and robber
    j = 0
    cop = 0
    robber = random.choice(range(cycle))
    print("Initial position of cop is ", cop)
    print("Initial position of robber is ", robber)
    # Game play
    while j >= 0:
        if cop == robber :
            print("Robber go to cop")
            break
        j += 1
# Cop strategies
        minus = abs((cop - robber) % cycle)
        add = abs((robber - cop) % cycle)
        print('add', add, 'minus', minus)
        if cop == (robber + 1) % cycle or cop == (robber - 1) % cycle:
            cop = robber
        elif add <= minus: cop = (cop + 1) % cycle
        else : cop = (cop - 1) % cycle
        print("position of cop in turn {} is ".format(j), cop)
        if cop == robber :
            print("Cop catch the robber")
            break
#Robber move
        move = random.choice([1,-1])
        robber = (robber + move) % cycle
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