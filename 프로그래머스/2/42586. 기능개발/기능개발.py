# 진도 - 스피드 
# 앞에 진도가 완성이어야 뒤 작업 완성 가능
# 완성되는 작업의 수를 순서대로 리턴 
# 큐를 이용
# 첫 작업이 100이 되면 pop left를 하고 다음 100이 아닌 수가 나올 때가지 pop left 
# 100이 아닌 수가 나오면 pop left한 개수를 answer. append 
# 그리고 다시 작업 speed만큼 완성도에 더해줌. 
# import collections
from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    sp = deque(speeds)
    cnt = 0
    while queue:
        # print(queue,answer)
        if queue[0] < 100:
            queue = deque(map(sum,zip(queue,sp)))
        elif queue[0] >= 100:
            queue.popleft()
            sp.popleft()
            cnt += 1
            continue
        answer.append(cnt) if cnt != 0 else None
        cnt = 0
    answer.append(cnt)
    
    return answer