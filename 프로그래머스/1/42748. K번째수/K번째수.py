def solution(array, commands):
    answer = []
    for c in commands:
        lst = sorted(array[c[0]-1:c[1]])
        # print(lst,c)
        answer.append(lst[c[2]-1])
    return answer