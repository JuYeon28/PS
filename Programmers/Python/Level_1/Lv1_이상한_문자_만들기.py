def solution(s):
    s_split = s.split(" ")
    
    for i in range(len(s_split)):
        s_list = list(s_split[i])
        
        for j in range(len(s_list)):
            if j%2 == 0:
                s_list[j] = s_list[j].upper()
            else:
                s_list[j] = s_list[j].lower()
        s_split[i] = "".join(s_list)
    answer = " ".join(s_split)
    return answer