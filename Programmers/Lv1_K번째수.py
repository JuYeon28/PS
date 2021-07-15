def solution(array, commands):
    
    answer = []
    for n in range(len(commands)):
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        
        numlist = sorted(array[i-1:j])        
        answer.append(numlist[k-1])
        
    return answer

#commands[n]인 [2, 5, 3]을 받을 때, i, j, k = commands[n]으로 개수만 맞추면 받아짐

if __name__=='__main__':
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])