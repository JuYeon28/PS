X, Y = map(str, input().split())

def Rev(n):
    n = str(n)
    n = n[::-1]
    return int(n)

print(Rev(Rev(X)+Rev(Y)))