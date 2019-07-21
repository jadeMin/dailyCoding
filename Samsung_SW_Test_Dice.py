N, M, x, y, K = input().split()
board = []

#2-Dimension input as list type
for i in range(0,N):
  temp = []
  for j in range(0,M):
    temp.append(input().split())
  board.append(temp)
  
#Blank input
