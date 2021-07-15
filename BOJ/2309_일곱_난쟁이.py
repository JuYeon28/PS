height = []

for i in range(9):
    height.append(int(input()))

sum_height = sum(height)
non_1 = 0
non_2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if sum_height - height[i] - height[j] == 100:
            non_1 = height[i]
            non_2 = height[j]

height.remove(non_1)
height.remove(non_2)

height = sorted(height)

for i in height:
    print(i)