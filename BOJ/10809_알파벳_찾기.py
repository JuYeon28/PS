S = list(input())

alpha_list = []
dup = []

for i in range(26):
    alpha_list.append(-1)

for i in range(len(S)):
    
    if S[i] not in dup:
        dup.append(S[i])
    else:
        continue
    alpha_list[(ord(S[i])-97)] = i

# for i in alpha_list:
#     print(i, end=" ")

print(*alpha_list) #List 각 원소를 일렬로 표시해야할 때 편한 방법