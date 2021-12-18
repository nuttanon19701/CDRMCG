import random
import math
# import the graph in dictionary key : Neighborhood of key
distance_of_devil = int(input('Distance Devil will enclosed '))
power = int(input('Power of angel '))

for j in range(distance_of_devil) :
    angel_win = 0
    number_of_iteration = 10000
    Time_taken = 0
    Total_number_of_block_devil_destroy = math.ceil(math.pi*(power +1)*(2*j+power-1))
    print(Total_number_of_block_devil_destroy)
    for i in range(number_of_iteration):
    # Initial position of cop and robber
        i = 0
        a_x = 0
        a_y = 0
        angel = (a_x,a_y)
        # Game play
        while i <= Total_number_of_block_devil_destroy:
            i += 1
    #Robber move
            dx = random.choice(range(-power,power+1))
            dy = random.choice(range(-power,power+1))
            a_x = a_x + dx
            a_y = a_y + dy
            angel = (a_x,a_y)
        d = math.sqrt(abs(a_x)**2 + abs(a_y)**2)
        #print('Final position of angel is', angel, 'with distance', d)
        if d > j+1 : angel_win += 1
    percentage = angel_win/number_of_iteration
    print('Angel win percentage is ', percentage, 'with power ', power, 'and devil enclosed with circle radius', j)
    print('######################################################')
