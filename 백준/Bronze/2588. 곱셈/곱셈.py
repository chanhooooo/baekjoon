mul1 = int(input())
mul2 = int(input())

print(mul1*(mul2%10))
print(mul1*(mul2%100//10))
print(mul1*(mul2//100))
print(mul1*(mul2%10) + mul1*(mul2%100//10)*10 + mul1*(mul2//100)*100)