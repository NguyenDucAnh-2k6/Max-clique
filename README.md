# Max-clique
Given an undirected graph G = (V, E). Find the largest subgraph of G which is a completed graph. <br />

Input <br />
Line 1: contains n and m which are the number of nodes and edges of G (1 <= n <= 100, 1 <= m <= 1000) <br />
Line i+1 (i = 1, 2,. . ., m): contains 2 positive integers u and v which are endpoints of the ith edge <br />
Output <br />
Line 1: Write the number of nodes of the complete subgraph found. <br />
Line 2: write a list of nodes of the subgraph found, separated by a SPACE character. <br />

Example <br />
Input  <br />
9  17 <br />
1 3 <br />
1 6 <br />
1 9 <br />
2 3 <br />
2 4 <br />
2 7 <br />
2 9 <br />
3 4 <br />
3 5 <br />
3 6 <br />
3 9 <br />
4 5  <br />
4 7 <br />
4 8 <br />
5 6 <br />
5 8 <br />
7 8 <br />


Output <br />
3 <br />
1 3 6 <br />
