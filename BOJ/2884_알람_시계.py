H, M = map(int, input().split())

M -= 45

if M >= 0:
    print(H, M)
else:
    M = 60 - abs(M)
    if H == 0 :
        H = 23
    else:
        H -= 1
    print(H, M)