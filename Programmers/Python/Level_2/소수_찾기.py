import math
from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
        

def solution(numbers):
    answer = []

    for i in range(1, len(numbers)+1):
        perlist = list(permutations(numbers, i))
        for j in range(len(perlist)):
            num = int(''.join(map(str, perlist[j])))
            if is_prime(num):
                answer.append(num)
    return len(set(answer))