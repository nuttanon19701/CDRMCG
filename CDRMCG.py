import random
# import the graph in dictionary key : Neighborhood of key
graph = { "a" : {"b", "f", "A"},
          "b" : {"a", "c", "B"},
          "c" : {"a", "b", "d", "e"},
          "d" : {"c"},
          "e" : {"c", "b"},
          "f" : {"c"}
          "A" : {"c"}
          "B" : {"c"}
          "C" : {"c"}
          "D" : {"c"}
          "E" : {"c"}
          "F" : {"c"}
        }
number_of_iteration = 10000
Time_taken = 0
for i in range(number_of_iteration):
# Initial position of cop and robber
    i = 0
    cop = 'a'
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
        Neighborhood_Cop = list(graph[cop])
        cop = random.choice(Neighborhood_Cop)
        print("position of cop in turn {} is ".format(i), cop)
        if cop == robber :
            print("Cop catch the robber")
            break
#Robber move
        Neighborhood_Robber = list(graph[robber])
        robber = random.choice(Neighborhood_Robber)
        print("position of robber in turn {} is ".format(i), robber)
    print('The time taken until the game end ', i)
    Time_taken = Time_taken + i
    print('######################################################')
Expected_capture_time = float(Time_taken) / number_of_iteration
print("The expected capture time of a graph G is ", Expected_capture_time)