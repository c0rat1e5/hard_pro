import numpy as np
import sys
# 距離K以内にxが居ない
# xからの距離を測る

buf = sys.stdin.buffer
R,C = map(int,buf.readline().split())
black = np.zeros((R+2,C+2),dtype=np.bool)
black[1:-1,1:] = (np.frombuffer(buf.read(R*(C+1)),dtype='S1') == b'#').reshape(R,C+1)

INF = 10 ** 9
dist = np.zeros((R,C),dtype=np.int32)
dist[~black[1:-1,1:-1]] = INF

for n in range(1,R):
  np.minimum(dist[n-1]+1,dist[n],out=dist[n])
for n in range(R-2,-1,-1):
  np.minimum(dist[n+1]+1,dist[n],out=dist[n])

for n in range(1,C):
  np.minimum(dist[:,n-1]+1,dist[:,n],out=dist[:,n])
for n in range(C-2,-1,-1):
  np.minimum(dist[:,n+1]+1,dist[:,n],out=dist[:,n])

answer = dist.max()
print(answer)
