#25304 영수증
# total price
X = int(input())
# item
N = int(input())
total = 0

for _ in range(N):
    a, b = map(int, input().split())
    total += a*b
if X - total == 0:
    print("Yes")
else:
    print("No")