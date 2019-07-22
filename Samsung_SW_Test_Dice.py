N, M, x, y, K = input().split()
board = []

#2-Dimension input as list type
for i in range(0,N):
  temp = []
  for j in range(0,M):
    temp.append(input().split())
  board.append(temp)
  
command = []

#Direction Commands input - east:1, west:2, north:3, south:4
for k in range(0,K):
  command.append(input().split())

#Number -> command
for c in command:
  if c == 1:
  
  elif c == 2:
  
  elif c == 3:
    
  elif == 4:
    
  else:
