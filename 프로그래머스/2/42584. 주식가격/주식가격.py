from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    while len(queue) > 1 :
        curr = queue.popleft()
        sec = 0
        for price in queue:
            sec += 1
            if curr > price:
                break
        answer.append(sec)
    answer.append(0)
            
    return answer