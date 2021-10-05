def solution(n):
    n_list = list(str(n))
    n_list.reverse()
    return list(map(int, n_list))