import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
import Graphcreate as graph
# import the graph in dictionary key : Neighborhood of key
# distance_between_cop_n_robber = int(input('Distance between cop and robber '))

number_of_iteration = 100000
Time_taken = []
start = []
n = int(input('the value of n is '))
m = int(input('the value of m is '))
graph = graph.grid2(n,m)

for i in range(number_of_iteration):
# Initial position of cop and robber
    i = 0
    c_x = int(np.ceil(n/2))
    c_y = int(np.ceil(m/2))
    cop = (c_x,c_y)
    robber = random.choice(list(graph.keys()))
    (r_x,r_y) = robber
    print("Initial position of cop is ", cop)
    print("Initial position of robber is ", robber)
    # Game play
    while i >= 0:
        if cop == robber:
            print("Robber go to cop")
            break
        i += 1
# Cop strategies
        #print('c_x is', c_x, 'c_y is ', c_y)
        #print('r_x is', r_x, 'r_y is ', r_y)
        diff_x = abs(c_x - r_x)
        diff_y = abs(c_y - r_y)
        #print('diff_x = ', diff_x, 'diff_y = ',diff_y)
        if  diff_y >= diff_x and c_y - r_y > 0: c_y = c_y - 1
        elif  diff_y >= diff_x and c_y - r_y < 0: c_y = c_y + 1
        elif diff_x >= diff_y and c_x - r_x > 0: c_x = c_x - 1
        else : c_x = c_x + 1
        #print('c_x is', c_x, 'c_y is ', c_y)
        cop = (c_x,c_y)
        print("position of cop in turn {} is ".format(i), cop)
        if cop == robber :
            print("Cop catch the robber")
            break
#Robber move
        robber = random.choice(list(graph[robber]))
        (r_x, r_y) = robber
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