results = []

while (True):
    nums = list(map(int, input().split()))

    if nums[0] == nums[1] == 0:
        for i in range(len(results)):
            print(results[i])
        break
    elif nums[1]%nums[0] == 0:
        results.append("factor")
    elif nums[0]%nums[1] == 0:
        results.append("multiple")
    else:
        results.append("neither")