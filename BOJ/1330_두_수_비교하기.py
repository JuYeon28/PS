AB = input()
A = int(list(AB.split(" "))[0])
B = int(list(AB.split(" "))[1])

if A<-10000 or B>10000:
    print("Input Error")
elif A>B:
    print(">")
elif A<B:
    print("<")
elif A==B:
    print("==")