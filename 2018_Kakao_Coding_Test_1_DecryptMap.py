#비트연산자를 활용하여 비밀 지도 풀기

n = int(input("n: "))

map1 = []
map2 = []
solution = []

print("First Map: ")
for i in range(n):
    map1.append(int(input()))
    
print("Second Map: ")
for i in range(n):
    map2.append(int(input()))

for i in range(n):
    solution.append(bin(map1[i] | map2[i])[2:].replace('0',' ').replace('1', '#'))

print(solution)
 
# Example
# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# 출력  ['#####', '# # #', '### #', '#__##', '#####']
