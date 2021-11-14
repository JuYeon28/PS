def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    for k, v in clothes_dict.items():
        answer *= v+1

    return answer-1