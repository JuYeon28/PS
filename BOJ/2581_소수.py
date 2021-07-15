M, N = int(input()), int(input())
nums = []
sums = 0

while(M<=N):
    for i in range(M+1):
        if i==0 or i==1:
            continue
        elif M%i==0 and i!=M:
            break
        elif i==M:
            nums.append(i)
    M += 1

if nums == []:
    print(-1)
else:
    for k in range(len(nums)):
        sums += nums[k]
    print(sums)
    print(nums[0])

#에라토스테네스의 체: 소수 찾는 알고리즘
#반복문의 M+1을 sqrt(M)+1로 둬야 훨씬 빠름