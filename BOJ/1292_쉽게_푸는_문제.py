A, B = map(int, input().split())

num_list = []

for i in range(1, 46):
    num_list += [i]*i
    
print(sum(num_list[A-1:B]))