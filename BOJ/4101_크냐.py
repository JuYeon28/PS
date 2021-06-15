numlist = []

while(True):
    A, B = map(int, input().split())
    if B<A:
        numlist.append("Yes")
    else:
        if A == 0 and B == 0:
            break
        else:
            numlist.append("No")

for i in range(len(numlist)):
    print(numlist[i])