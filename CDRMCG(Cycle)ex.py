import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
from itertools import islice

# Input the number of vertices in each multipartite
cycle = int(input("The number of vertices in cycle "))
ex = []
yerrs = []
th = []
for k in range(3,cycle+1):
    number_of_iteration = 100000
    Time_taken = []
    for i in range(number_of_iteration):
    # Initial position of cop and robber
        j = 0
        cop = 0
        robber = random.choice(range(k))
       # print("Initial position of cop is ", cop)
       # print("Initial position of robber is ", robber)
        # Game play
        while j >= 0:
            if cop == robber :
                #print("Robber go to cop")
                break
            j += 1
    # Cop strategies
            minus = abs((cop - robber) % k)
            add = abs((robber - cop) % k)
           # print('add', add, 'minus', minus)
            if cop == (robber + 1) % k or cop == (robber - 1) % k:
                cop = robber
            elif add <= minus: cop = (cop + 1) % k
            else : cop = (cop - 1) % k
           # print("position of cop in turn {} is ".format(j), cop)
            if cop == robber :
                #print("Cop catch the robber")
                break
    #Robber move
            move = random.choice([1,-1])
            robber = (robber + move) % k
           # print("position of robber in turn {} is ".format(j), robber)
       # print('The time taken until the game end ', j)
        Time_taken.append(j)
        #print('######################################################')
    Expected_capture_time = statistics.mean(Time_taken)
    print("The expected capture time of a cycle graph G of {} is ".format(k), Expected_capture_time)
    print("The Standard Error is ", sem(Time_taken))
    SE = sem(Time_taken)
    yerrs.append(SE)
    if k % 2 == 1:
        dct = k / 4 - 1 / (4 * k)
    else:
        dct = k / 4
    print('the Theoretical result is', dct)
    diff = Expected_capture_time - dct
    ex.append(diff)
    print('######################################################')

expoint = np.array(ex)
yerrpoint = np.array(yerrs)
xpoint = list(range(3,cycle+1))
plt.errorbar(xpoint, ex, yerr = yerrpoint, fmt='.k')
plt.plot(xpoint, ex, '-o')
plt.show()