A, B, C = map(int, input().split())

if (A == B) and (B == C):
    print(f"{10000 + A*1000}")
elif (A == B) and (B != C) or ((A == C) and (B != C)):
    print(f"{1000+ A*100}")
elif (A != B) and (B == C):
    print(f"{1000+ B*100}")
elif A != B != C:
    if A > B and A > C:
        print(f"{100*A}")
    elif B > A and B > C:
        print(f"{100*B}")
    elif C > A and C > B:
        print(f"{100*C}")