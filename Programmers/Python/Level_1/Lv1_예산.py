def solution(d, budget):
    result = 0
    d.sort()
    for i in range(len(d)):
        budget -= d[i]    
        if budget < 0:
            break
        else:
            result += 1
    return result