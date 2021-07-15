def solution(strings, n):
    return sorted(strings, key = lambda x : (x[n], x.lower()))

if __name__=='__main__':
    solution(["abce", "abcd", "cdx"], 2)
    #solution(["car", "bed", "sun"], 1)