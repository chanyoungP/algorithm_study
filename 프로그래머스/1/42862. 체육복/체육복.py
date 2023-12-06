def solution(n, lost, reserve):
    answer = 0
    both = set(lost) & set(reserve)
    # print(both)
    lost = sorted(list(filter(lambda x : x not in both,lost)))
    reserve = sorted(list(filter(lambda x : x not in both, reserve)))
    # print(lost,reserve)
    
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            n -= 1 
    return n