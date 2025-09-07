#10811 바구니 뒤집기

N, M = map(int, input().split())

arr1 = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    arr1[i-1:j] = arr1[i-1:j][::-1]

print(*arr1)
