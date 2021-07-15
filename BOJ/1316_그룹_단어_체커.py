input_num = int(input())

num = 0

for i in range(input_num):
    input_ = input()
    for j in range(len(input_)):
        if j != len(input_)-1:
            if input_[j] == input_[j+1]:
                pass
            elif input_[j] in input_[j+1:]:
                break
        else:
            num += 1
print(num)