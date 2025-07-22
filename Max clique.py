import sys
def Input():
    f=sys.stdin
    [n,m]=[int(x) for x in f.readline().split()]
    graph=[[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        [u,v]=[int(x) for x in f.readline().split()]
        graph[u-1][v-1]=True
        graph[v-1][u-1]=True
    return n, graph
def inputfile(filename):
    with open(filename, 'r') as f:
        [n,m]=[int(x) for x in f.readline().split()]
        graph=[[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            [u,v]=[int(x) for x in f.readline().split()]
            graph[u-1][v-1]=True
            graph[v-1][u-1]=True
    return n, graph
def is_clique(clique, graph):
    for i in range(len(clique)):
        for j in range(i+1, len(clique)):
            if graph[clique[i]][clique[j]]==0:
                return False
    return True
def Try(curr, start, n, graph):
    global max_clique
    for i in range(start,n):
        new_clique=curr+[i]
        if is_clique(new_clique, graph):
            if len(new_clique)>len(max_clique):
                max_clique=new_clique[:]
            Try(new_clique, i+1,n,graph)
n,graph=inputfile('Max clique data.txt')
#n,graph=Input()
max_clique=[]
Try([],0,n,graph)
res=[x+1 for x in max_clique[:]]
print(len(res))
for i in range(len(res)):
    print(res[i], end=' ')
