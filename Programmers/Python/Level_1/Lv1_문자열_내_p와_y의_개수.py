def solution(s):
    p = s.count('p')
    P = s.count('P')
    y = s.count('y')
    Y = s.count('Y')
    
    if p+P == y+Y:
        return True
    else:
        return False