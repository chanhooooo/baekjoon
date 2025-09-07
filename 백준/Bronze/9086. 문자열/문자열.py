#9086 문자열

N = int(input())
str1 = []
for i in range(N):
    str1.append(input())

for word in str1:
    print(word[0], end="")
    print(word[-1])