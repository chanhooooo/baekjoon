###### 1546 평균

N = int(input())

arr1 = list(map(int, input().split()))

M = arr1[0]

for i in range(1, N):
    if M < arr1[i]:
        M = arr1[i]
        
total = 0

for i in range(N):
    jo = (arr1[i]/M)*100
    total += jo

print(total/N)