#Max clique ortools version
import sys
from ortools.sat.python import cp_model
def Input():
    f=sys.stdin
    [n,m]=[int(x) for x in f.readline().split()]
    graph=[[0 for _ in range(n)] for _ in range(n)]
    edges=[]
    for _ in range(m):
        [u,v]=[int(x) for x in f.readline().split()]
        edges.append([u,v])
        graph[u-1][v-1]=True
        graph[v-1][u-1]=True
    return n, m, edges, graph
def inputfile(filename):
    with open(filename, 'r') as f:
        [n,m]=[int(x) for x in f.readline().split()]
        graph=[[0 for _ in range(n)] for _ in range(n)]
        edges=[]
        for _ in range(m):
            [u,v]=[int(x) for x in f.readline().split()]
            edges.append([u,v])
            graph[u-1][v-1]=True
            graph[v-1][u-1]=True
    return n, m, edges, graph
#n,m,edges,graph=Input()
n,m,edges, graph=inputfile('Max clique data.txt')
#Build model
model=cp_model.CpModel()
#Declare decision vars
x=[model.NewBoolVar('x[{i}]') for i in range(n)]
#Declare constraints
#Build adjacency sets
adj=[set() for _ in range(n)]
for [u,v] in edges:
    adj[u-1].add(v-1)
    adj[v-1].add(u-1)
for i in range(n):
    for j in range(i+1,n):
        if j not in adj[i]:
            model.Add(x[i]+x[j]<=1)
model.Maximize(sum(x))   #Objective func
#Declare solver
solver=cp_model.CpSolver()
status=solver.Solve(model)
if status==cp_model.OPTIMAL or status==cp_model.FEASIBLE:
    clique=[i+1 for i in range(n) if solver.Value(x[i])]
    print(len(clique))
    print(*clique)
else:
    print("0\n")
