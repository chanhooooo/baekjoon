# 2439 별 찍기 - 2

N = int(input())

for i in range(1, N+1):
    #1 2 3 4 5
    for _ in range(N-i):
    #4 3 2 1 0
        print(" ", end= "")
    for _ in range(i):
        #1 2 3 4 5
        print("*", end = "")
    print("")