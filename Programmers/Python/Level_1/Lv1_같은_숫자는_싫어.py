def solution(arr):
    answer = []
    
    answer.append(arr[0])

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
        else:
            continue
        
    return answer