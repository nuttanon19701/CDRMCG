from itertools import islice

def grid2(n,m):
    all_states = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            all_states.append((i, j))
    graph = {}
    for v in all_states:
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        neighbors = []
        for dir in dirs:
            neighbor = (v[0] + dir[0], v[1] + dir[1])
            if 1 <= neighbor[0] <= n and 1 <= neighbor[1] <= m:
                neighbors.append(neighbor)
        graph[v] = neighbors
    return graph

def multipartite():
    Input = input("The number of vertices in each partite (ex. 1,2,2 ) ")
    No_Partite = list(int(x) for x in Input.split(","))
    total_vertex = sum(list(No_Partite))
    total_partite = len(No_Partite)
    Set_of_vertex = list(range(total_vertex))
    it_Set_of_vertex = iter(Set_of_vertex)
    Set_of_partite = list(map(chr, range(ord('A'), ord('A') + total_partite)))
    Set_of_vertex2 = [set(islice(it_Set_of_vertex, elem))
                      for elem in No_Partite]
    Vertex_in_partite = {}
    for i in range(total_partite):
        Vertex_in_partite[Set_of_partite[i]] = Set_of_vertex2[i]
    graph = {}
    for partite in Vertex_in_partite:
        for elem in Vertex_in_partite[partite]:
            O = set(Set_of_vertex)
            graph[elem] = list(O - Vertex_in_partite[partite])
    return graph

def cycle(n):
    all_states = range(1,n+1)
    graph = {}
    for v in all_states:
        i = all_states.index(v)
        graph[v] = [all_states[(i-1)%n], all_states[(i+1)%n]]
    return graph

def prism(n):
    all_states = range(1,2*n+1)
    graph = {}
    for v in all_states:
        i = all_states.index(v)
        if v > n: graph[v] = sorted([all_states[(i-1)%n + n], all_states[(i+1)%n + n], all_states[i - n]])
        else: graph[v] = sorted([all_states[(i-1)%n], all_states[(i+1)%n], all_states[i + n]])
    return graph