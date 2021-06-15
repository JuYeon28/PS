nums = input()
num_list = list(nums.split(" "))
n_sum = 0

for i in range(5):
    num = int(num_list[i])
    sq = num**2
    n_sum += sq

ver = n_sum%10
print(ver)