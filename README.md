
# The cop and drunk robber game package

In this file, we provide a guideline to use our Python package 
which aims to find the averages of numbers of turns (expected capture times) 
that a single cop needs to catch a drunk robber who performs a symmetric random walks 
in many classes of graphs. Basically, the game has two players, the cop and the drunk 
robber. The players alternately play by moving from their current position (vertices) 
to a neighbor. The game ends if the cop is on the same vertex as the drunk robber and 
we count the number of turns.

This package implements some results in
-	Quilliot, A., 1985, "Jeux et pointes fixes sur les graphes, th`ese de 3`eme cycle [Games and fixed points on graphs, Ph.D. Thesis]", Universite de Paris VI, pp. 131-145 (in French).
-	Kehagias, A. and Pralat, P., 2012, "Some remarks on cops and drunk robbers", Theoretical Computer Science, Vol. 463, pp. 133-147.

and all the results in
-	Songsuwan, N. and Kaemawichanurat, P. 2022, "Chasing a Drunk Robber in Many Classes of Graphs", submitted to Dynamic Games and Applications.

We may give an example to compile our programs as follows: to compute expected capture time when the game is played on prism graph P2 box Cn (the lexicographic product between P2 and Cn), user may open 
“CDRMCG(Prism Graph).py”. 
After that, the screen shows 
“The number of vertices in cycle _” 
which user may insert some positive integer which will be the order of Cn. Then press “enter” and the screen will finally shows the expected capture time together with the standard error in the two bottom lines. The program also illustrates the histogram that shows the frequencies of the number of turns to end all the games. Please note that the program was set to run 100,000 times. 
