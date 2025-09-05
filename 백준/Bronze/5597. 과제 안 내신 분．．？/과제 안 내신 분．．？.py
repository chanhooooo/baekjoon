# 5597 과제 안 내신 분..?
students = []
array1 = []
for _ in range(28):
    i = int(input())
    students.append(i)

for i in range(1,31): 
    c = students.count(i)
    if(c == 0):
        print(i)
