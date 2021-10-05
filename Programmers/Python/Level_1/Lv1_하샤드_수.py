def solution(x):
    sum_ = 0
    x_ori = x
    while x>0:
        n = x%10
        sum_ += n
        x //= 10

    if x_ori % sum_ == 0:
        return True
    else:
        return False