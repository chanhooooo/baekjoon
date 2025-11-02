#1316 그룹 단어 체커

N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append(word)
    
total_count = 0

for word in words:
    seen = []
    prev_char = ''
    
    for current_char in word:
        
        if current_char != prev_char:
            
            if current_char in seen:
                break 
            else:
                seen.append(current_char)
        
        prev_char = current_char
        
    else: 
        total_count += 1

print(total_count)