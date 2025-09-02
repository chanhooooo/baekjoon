#2562 최댓값


array1 = []

for _ in range(9):
    N = int(input())
    array1.append(N)

Max = array1[0]
idx = 1

for i in range(1, 9):
    if(Max < array1[i]):
        Max = array1[i]
        idx = i + 1
print(Max)
print(idx)