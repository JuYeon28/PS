dish = list(input())
length = 10

for i in range(len(dish)-1):
    if dish[i] == dish[i+1]:
        length += 5
    else:
        length += 10

print(length)