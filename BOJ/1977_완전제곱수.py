M, N = int(input()), int(input())

i = 0
nums = []
sums = 0

while (i**2 < M):
    i += 1

min_num = i**2
    
while (i**2 <= N):
    nums.append(i**2)
    i += 1
    
if i**2 == min_num:
    print(-1)
else:
    for k in range(len(nums)):
        sums += nums[k]
    print(sums)
    print(min_num)

#M에서부터 시작해서 첫 제곱수를 찾는 방법 - 찾으면 걔를 1씩 증가시키면서 N보다 작은 제곱수까지를 찾음
#M과 N을 sqrt()해서 각각 올림, 내림 후 그 사이 값들을 찾음