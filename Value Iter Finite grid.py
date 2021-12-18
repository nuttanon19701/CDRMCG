# import math
# import numpy as np
import CADRfunction as CADR
import Graphcreate as graph
import Markov as mkv
# Transition matrix #
graph = graph.prism(250)
print('graph = ', graph)
P = mkv.transition(graph)
print('P = ', P)
U1, Cd = CADR.cadr(graph,1000,0.000001)
# print('P= ', P)
print('U = ', U1)
print('C = ', Cd)

D = CADR.dct(Cd)
cop = CADR.copint(graph, Cd)
print('the drunken capture time (dct) is ', D)
print('the initial position of cop is ', cop)
