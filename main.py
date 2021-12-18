import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem
distance_between_cop_n_robber = 3
start = []
for i in range(distance_between_cop_n_robber + 1) :
    r = (distance_between_cop_n_robber - i, i)
    rn = (distance_between_cop_n_robber - i, -i)
    nr = (-distance_between_cop_n_robber + i, i)
    nrn = (-distance_between_cop_n_robber + i, -i)
    start.append(r)
    start.append(rn)
    start.append(nr)
    start.append(nrn)

start = list( dict.fromkeys(start) )
print(start)
S = dict.fromkeys(start,0)
number_of_iteration = 10000
for i in range(number_of_iteration):
    R = random.choice(start)
    S[R] = S[R] + 1
S_value = S.values()
S_value_list = list(S_value)
print(S_value_list)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(start,S_value_list)
plt.show()