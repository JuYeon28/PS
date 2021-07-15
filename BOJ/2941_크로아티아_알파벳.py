input_str = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro:
    input_str = input_str.replace(i, "*")

print(len(input_str))