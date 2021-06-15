s_sum = 0

for i in range(5):
    score = int(input())
    
    if score<0 or score>100 or score%5!=0:
        print("Input Error")
    elif score<40:
        score =40
        s_sum += score
    else:
        s_sum += score

print(int(s_sum/5))