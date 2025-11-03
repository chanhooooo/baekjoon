#2738 행렬 덧셈

N, M = map(int, input().split(" "))
arr1 = []
arr2 = []
result = []

for _ in range(N):
    row = list(map(int, input().split(" ")))
    arr1.append(row)
for _ in range(N):
    row = list(map(int, input().split(" ")))
    arr2.append(row)
    
for i in range(N):
    new_row = []
    for j in range(M):
        sum_val = arr1[i][j] + arr2[i][j]
        new_row.append(sum_val)
    result.append(new_row)
for row in result:
    print(*row)