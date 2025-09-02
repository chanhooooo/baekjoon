# 첫 줄: 정수의 개수
N = int(input())

# 둘째 줄: 정수 리스트
numbers = list(map(int, input().split()))

# 셋째 줄: 찾으려는 정수
v = int(input())

# 개수 세기
count = numbers.count(v)

print(count)
