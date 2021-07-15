inputs = []

for i in range(int(input())):
    inputs.append(input().split())

for i in range(len(inputs)):
    outputs = []
    for j in range(len(inputs[i][1])):
        S = inputs[i][1][j]*int(inputs[i][0])
        outputs.append(S)
    print("".join(outputs))