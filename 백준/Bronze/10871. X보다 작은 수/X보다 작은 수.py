#10871 X보다 작은 수

N, X = map(int, input().split())

array1 = list(map(int, input().split()))

for arr in array1:
    if(X>arr):
        print(arr, end = " ")