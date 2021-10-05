def solution(n):
    answer = []
    
    for i in range(n+1):
        if i > 0:
            if n % i == 0:
                answer.append(i)
    
    return sum(answer)