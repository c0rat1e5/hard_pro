import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

H,W,N = map(int,readline().split())

grid = np.frombuffer(read(),'S1').reshape(H,-1)[:,:W].ravel()

ind = [np.where(grid==b'S')[0][0]]
for n in range(1,N+1):
    ind.append(np.where(grid==str(n).encode())[0][0])

def grid_graph_edges(H,W):
    idx = np.arange(H*W).reshape(H,W)
    fr = []
    to = []
    x1 = idx[:,1:].ravel()
    x2 = idx[:,:-1].ravel()
    fr += [x1,x2]
    to += [x2,x1]
    x1 = idx[1:,:].ravel()
    x2 = idx[:-1,:].ravel()
    fr += [x1,x2]
    to += [x2,x1]
    fr = np.concatenate(fr)
    to = np.concatenate(to)
    return fr,to

fr,to = grid_graph_edges(H,W)

bl = (grid[fr] != b'X')&(grid[to] != b'X')
fr = fr[bl]; to = to[bl]

graph = csr_matrix((np.ones(len(fr)),(fr,to)),(H*W,H*W))
dist = dijkstra(graph,directed=False,indices=ind[:-1])

answer = sum(int(dist[i,x]) for i,x in enumerate(ind[1:]))
print(answer)
