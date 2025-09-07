#11720 숫자의 합

N = int(input())
arr1 = []
arr1 = list(map(int, input()))

total = 0

for i in arr1:
    total += i
print(total)