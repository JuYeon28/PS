def solution(a, b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
       
    answer = day[(sum(month[:a-1])+b-1)%7]
    
    return answer