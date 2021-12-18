import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
# import the graph in dictionary key : Neighborhood of key
distance_between_cop_n_robber = int(input('Distance between cop and robber '))

number_of_iteration = 100000
Time_taken = []
for i in range(number_of_iteration):
# Initial position of cop and robber
    i = 0
    c_x = 0
    c_y = 0
    c_z = 0
    cop = (c_x,c_y,c_z)
    r_x = random.choice(range(-distance_between_cop_n_robber , distance_between_cop_n_robber + 1))
    r_y = random.choice(range(-distance_between_cop_n_robber + abs(r_x) , distance_between_cop_n_robber - abs(r_x)+1))
    r_z = random.choice([distance_between_cop_n_robber - abs(r_x) - abs(r_y) , - distance_between_cop_n_robber + abs(r_x) + abs(r_y)])
    robber = (r_x,r_y,r_z)
    print("Initial position of cop is ", cop)
    print("Initial position of robber is ", robber)
    # Game play
    while i >= 0:
        if cop == robber :
            print("Robber go to cop")
            break
        i += 1
# Cop strategies
        diff_x = abs(c_x - r_x)
        diff_y = abs(c_y - r_y)
        diff_z = abs(c_z - r_z)
        if diff_x >= diff_y and diff_x >= diff_z and c_x - r_x > 0 : c_x = c_x - 1
        elif diff_x >= diff_y and diff_x >= diff_z and c_x - r_x < 0 : c_x = c_x + 1
        elif diff_y >= diff_x and diff_y >= diff_z and c_y - r_y > 0 : c_y = c_y - 1
        elif diff_y >= diff_x and diff_y >= diff_z and c_y - r_y < 0: c_y = c_y + 1
        elif diff_z >= diff_x and diff_z >= diff_y and c_z - r_z > 0: c_z = c_z - 1
        else : c_z = c_z + 1
        cop = (c_x,c_y,c_z)
        print("position of cop in turn {} is ".format(i), cop)
        if cop == robber :
            print("Cop catch the robber")
            break
#Robber move
        (dx,dy,dz) = random.choice([(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)])
        r_x = r_x + dx
        r_y = r_y + dy
        r_z = r_z + dz
        robber = (r_x,r_y,r_z)
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