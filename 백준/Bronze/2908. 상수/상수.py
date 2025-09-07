#2908 상수


N, M = input().split()

arr1, arr2 = [], []
rev1, rev2 = [], []
for i in N:
    arr1.append(i)
for i in M:
    arr2.append(i)

arr1 = arr1[::-1]
arr2 = arr2[::-1]

num1 = int(''.join(map(str, arr1)))
num2 = int(''.join(map(str, arr2)))

if num1 > num2:
    print(num1)
else:
    print(num2)