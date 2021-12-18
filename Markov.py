import numpy as np
def transition(graph):
    all_states = list(graph.keys())
    k = len(all_states)
    P = np.zeros( (k,k) )
    for v in all_states:
        for e in graph.get(v):
            x = all_states.index(v)
            y = all_states.index(e)
            P[x][y] = 1/len(graph.get(v))
    return P

