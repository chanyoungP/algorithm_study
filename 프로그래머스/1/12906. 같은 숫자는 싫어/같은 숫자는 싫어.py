def solution(arr):
    answer = []
    for n in arr:
        # print(answer)
        if not answer:
            answer.append(n)
        elif answer[-1] == n:
            answer.pop()
            answer.append(n)
        else:
            answer.append(n)
    return answer