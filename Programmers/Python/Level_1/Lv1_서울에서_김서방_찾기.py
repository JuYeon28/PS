def solution(seoul):
    if "Kim" in seoul:
        idx = seoul.index("Kim")
        return "김서방은 " + str(idx) + "에 있다"