# n중 for문 대신 combinations 사용

from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

summation = []

a= list(combinations(numbers,3)) #combination한 요소들을 직접 보려면 list로 꼭 묶어야 함, 연산은 정상적으로 수행
for i in a:
    sum_ = sum(i)
    if sum_ <= M:
        summation.append(sum_)
        
print(max(summation))

# Brute-Force 문제일 경우 무조건 combinations or permutations 사용

"""
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

summation = []

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j<=i or k <= j:
                continue
            else:
                sum_ = numbers[i]+numbers[j]+numbers[k]
                if sum_ <= M:
                    summation.append(sum_)

print(max(summation))
"""