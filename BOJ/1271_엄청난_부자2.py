inputs = list(str(input()).split(" "))
n = int(inputs[0])
m = int(inputs[1])

if m<1 or m>n or n>10**1000:
    print("Input Error")
else:
    print(n//m)
    print(n%m)