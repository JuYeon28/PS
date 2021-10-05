def solution(answers):
    one, two, three = [], [], []
    dicts = {1 : 0, 2 : 0, 3 : 0}

    for i in range(len(answers)):
        one.append(i%5+1)

        if i%2==0:
            two.append(2)
        elif i%8==5:
            two.append(4)
        elif i%8==7:
            two.append(5)
        else:
            two.append(i%8)

        if i%10<2:
            three.append(3)
        elif 2 <= i%10 < 6:
            three.append(i//2%5)
        elif 6 <= i%10 < 8:
            three.append(4)
        else:
            three.append(5)

    for i in range(len(answers)):
        if one[i] == answers[i]:
            dicts[1] += 1
        if two[i] == answers[i]:
            dicts[2] += 1
        if three[i] == answers[i]:
            dicts[3] += 1

    answer = [k for k, v in dicts.items() if v == max(list(dicts.values()))]
    
    return sorted(answer)

if __name__=='__main__':
    solution([1, 2, 3, 4, 5, 2, 4, 4, 5, 5, 3])