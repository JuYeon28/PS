import math

def solution(n):
    num = math.sqrt(n)

    if num == int(num):
        return int((num+1)**2)
    else:
        return -1

if __name__=='__main__':
    solution(144)