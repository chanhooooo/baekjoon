S = input()
result = [-1] * 26 

for i, ch in enumerate(S):    
    idx = ord(ch) - ord('a')   
    if result[idx] == -1:     
        result[idx] = i

print(*result)
