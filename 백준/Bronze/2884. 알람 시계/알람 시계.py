#2884 알람 시계

H, M = map(int, input().split())

if M >= 45:
    print(f"{H} {M-45}")
elif H>=1 and M <= 44:
    print(f"{H-1} {M+15}")
elif H == 0 and M <= 44:
    print(f"23 {M+15}")