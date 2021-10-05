import math

def solution(n):
    answer = 0
    for i in range(n+1):
        if prime(i) and i>1:
            answer+=1
    
    return answer

def prime(num):
    sqrt_ = int(math.sqrt(num))
    for i in range(2, sqrt_+1):
        if num%i == 0:
            return False
    return True