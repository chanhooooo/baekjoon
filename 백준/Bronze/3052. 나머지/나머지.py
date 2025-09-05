arr1 = []
for _ in range(10):
    N = int(input())
    arr1.append(N%42)

print(len(set(arr1)))