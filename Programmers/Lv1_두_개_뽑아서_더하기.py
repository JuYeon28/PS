def solution(numbers):
    sumlist = []

    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            sum_ = numbers[i]+numbers[i+j+1]
            sumlist.append(sum_) # 내장함수 이름을 변수명으로 사용하면, 그 이후 해당 내장함수는 사용할 수 x
            
    return sorted(list(set(sumlist)))
    
if __name__=='__main__':
    solution([5, 0, 2, 7])