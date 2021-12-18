import numpy as np
import Markov as mkv


def cadr(graph, T, threshold):
    # This function get matrix U and C
    # U is the matrix of the optimal play for cop from the i position and robber in j position (cop,robber)
    # C is the matrix of the expected capture time start from the position (cop,robber)
    # graph is the dictionary with keys is the vertex and value is the neighborhood of keys
    # T is the maximum number of iteration
    # threshold is the threshold to break the iteration
    P = mkv.transition(graph)
    all_states = list(graph.keys())
    C = np.zeros((len(P), len(P)))
    U = np.zeros((len(P), len(P)))
    PP = P.copy()
    t = 0
    while t < T:
        C_old = C.copy()
        C_new = C.copy()
        U_new = U.copy()
        for mc in all_states:
            for mr in all_states:
                if mr != mc:
                    C1 = 10000
                    U1 = 0
                    # print('mr = ', mr, 'mc = ', mc)
                    Nc = graph.get(mc)
                    for nc in Nc:
                        C2 = 1
                        P2 = P.copy()
                        P2[all_states.index(nc)] = 0
                        P2[:, all_states.index(nc)] = 0
                        Nr = graph.get(mr)
                        # print('Nr = ', Nr)
                        for nr in Nr:
                            # print('nr = ', nr)
                            C2 = C2 + P2[all_states.index(mr)][all_states.index(nr)] * C[all_states.index(nc)][
                                all_states.index(nr)]
                            # print(C2)
                        if C2 < C1:
                            C1 = C2
                            U1 = nc
                    # print('mc = {} and index is '.format(mc), all_states.index(mc))
                    C_new[all_states.index(mc)][all_states.index(mr)] = C1
                    U_new[all_states.index(mc)][all_states.index(mr)] = all_states.index(U1) + 1
        C = C_new.copy()
        U = U_new
        change = np.amax(np.abs(C - C_old))
        t += 1
        print('t = {} change = '.format(t), change)
        if change < threshold: break
    return U, C


def dct(Cd):
    # function: to find the drunken capture time of the graph
    # Cd is the array of cop-optimal expected capture time when cop at position i and robber at position j
    k = len(Cd)
    dct_x = np.sum(Cd, axis=1) / k
    result = np.min(dct_x)
    return result


def copint(graph, Cd):
    # function: to find the optimal position of the cop
    k = len(Cd)
    all_state = list(graph.keys())
    dct_x = list(np.sum(Cd, axis=1) / k)
    x_min = 100000
    y_min = 100000
    print(dct_x)
    for x in dct_x:
        if x < x_min:
            x_min = x
            i = dct_x.index(x_min)
            y_min = all_state[i]
    return y_min
