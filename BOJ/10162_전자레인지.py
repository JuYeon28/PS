T = int(input())
A, B, C = 0, 0, 0

if T >= 300:
    A, T = divmod(T, 300)
if T >= 60:
    B, T = divmod(T, 60)
C, T = divmod(T, 10)

if T == 0:
    print(A, B, C)
else:
    print(-1)