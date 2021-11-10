def solution(numbers):    
    numbers_list = list(map(str, numbers))
    numbers_list.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(numbers_list)))