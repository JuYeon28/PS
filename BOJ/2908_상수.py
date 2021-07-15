M, N = map(str, input().split())

M = M[::-1]
N = N[::-1]

if M>N:
    print(M)
else:
    print(N)