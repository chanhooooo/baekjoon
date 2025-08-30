# 2438 별 찍기 - 1

N = int(input())

for i in range(1, N+1):
    for _ in range(i):
        print("*", end = "")
    print("")