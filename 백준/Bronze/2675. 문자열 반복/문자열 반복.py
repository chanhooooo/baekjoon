#2675 문자열 반복
M = int(input())

for _ in range(M):
    N, arr = input().split()
    N = int(N)
    arr = list(arr)
    for i in arr:
        print(i*N, end = "")
    print()
    