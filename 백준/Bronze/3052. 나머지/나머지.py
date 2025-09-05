#3052 나머지

arr1 = []
for _ in range(10):
    N = int(input())
    arr1.append(N%42)
uniqe = []
for x in arr1:
    if x not in uniqe:
        uniqe.append(x)

print(len(uniqe))