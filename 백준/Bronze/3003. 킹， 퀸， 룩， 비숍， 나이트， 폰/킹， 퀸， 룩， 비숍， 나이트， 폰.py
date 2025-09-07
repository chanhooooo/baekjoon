#3003 킹, 퀸, 룩, 비숍, 나이트, 폰
chess = [1,1,2,2,2,8]
peieces = list(map(int, input().split()))
arr1 = []
for c,p in zip(chess, peieces):
    arr1.append(c-p)
print(*(arr1))