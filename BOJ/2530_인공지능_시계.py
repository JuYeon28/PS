hour, minute, second = map(int, input().split())
time = int(input())

minute2, second2 = divmod(second+time, 60)

hour2, minute3 = divmod(minute+minute2, 60)

hour3 = (hour+hour2)%24

print(f"{hour3} {minute3} {second2}")