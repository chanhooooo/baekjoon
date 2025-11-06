#2566 최댓값

arr2 = []
for _ in range(9):
    row = list(map(int, input().split(" ")))
    arr2.append(row)

max_value = arr2[0][0]
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if(arr2[i][j] > max_value):
            max_value = arr2[i][j]
            row = i
            col = j
print(max_value)
print(row+1, col+1)