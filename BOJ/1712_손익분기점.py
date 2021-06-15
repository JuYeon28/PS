inputs = list(input().split(" "))
A = int(inputs[0]) # 고정 비용
B = int(inputs[1]) # 가변 비용 (노트북 한 대 생성 시 추가 비용)
C = int(inputs[2]) # 노트북 한 대 값
n = 0 # 노트북 판매수

if A>21*(10**8) or B>21*(10**8) or C>21*(10**8):
    print("Input Error")
else:
    if B>=C:
        n = -1
    else:
        n = A/(C-B) + 1
    print(int(n))