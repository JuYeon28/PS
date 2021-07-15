A, B, V = map(int, input().split())

x = (V-B) / (A-B)

if x == int(x):
    print(int(x))
else:
    print(int(x)+1)


#per = A - B
#dis, day = 0, 1

#while (dis+A<V):
#    day += 1
#    dis += per
#print(day)