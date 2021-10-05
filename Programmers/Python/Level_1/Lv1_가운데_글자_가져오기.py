def solution(s):
    answer = ''
    idx = 0
    
    if len(s)%2 == 1:
        idx = int(len(s)/2)
        answer = s[(idx)]
    else:
        idx1, idx2 = int(len(s)/2 - 1), int(len(s)/2)
        answer = s[idx1:idx2+1]

    return answer