#10818 최소, 최대

N = int(input())

array1 = list(map(int, input().split()))

Min = array1[0]
Max = array1[0]

for i in range(1, N):
    if(Min > array1[i]):
        Min = array1[i]
        
for i in range(1, N):
    if(Max < array1[i]):
        Max = array1[i]

print(Min, end= " ")
print(Max)