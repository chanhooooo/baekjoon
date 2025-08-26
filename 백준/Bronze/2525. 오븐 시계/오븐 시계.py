#2525 오븐 시계
A, B = map(int, input().split())
C = int(input())

H = C // 60
M = C % 60

if A + H <= 23 and B + M <60:
    print(f"{A + H} {B + M}")
elif A + H + 1 <= 23 and B + M >= 60:
    print(f"{A + H + 1} {B + M - 60}")
elif A + H >= 24 and B + M <60:
    print(f"{A + H - 24} {B + M}")
elif A + H + 1 >= 24 and B + M >= 60:
    print(f"{A + H - 23} {B + M - 60}")