# 우선순위 가 높은 순서대로 실행 -> 같은 경우 이전 실행 순서대로 
# location은 처음 프로세스의 위치 0이면 A 
# location이 0이면 A 프로세스가 몇 번째로 실행되는지 리턴 
# 
# 인덱스로 위치를 프로세스 이름으로 
# 대기 큐에서 프로세스 꺼내서 우선순위가 높은 프로세스가 있다면 그 프로세스를 꺼냄 



'''
(인덱스, 우선순위)를 가지는 리스트를 deque로 생성을 한다.
*** 우선순위 max값 추출을 위해서 priorities를 정렬하고 deque로 생성(더 효율적인 방법을 모르겠음)
실행 순서를 담기위한 complete 리스트 생성

queue에 값이(인덱스,우선순위) 있는 동안 반복문 실행
    정렬한 리스트의 첫번째 값은 가장 큰 우선순위의 값,, 이를 변수에 할당
    그 변수랑 queue의 첫번째 요소의 우선순위 값하고 비교 
        같으면 그 작업이 가장 우선순위가 높은 작업 
            --> popleft해주고 complete에 index append
            --> 비교를 위해서 정렬한 deque 역시 popleft(다음 우선순위 추출을 위함)
        다르면 그 작업보다 우선순위가 높은 작업이 존재 --> rotate(-1) 왼쪽으로 shift
    위 과정을 반복하다보면 우선순위가 높은 순서대로 작업을 진행하고 우선순위가 같은 경우 원래 담겨 있던 순서대로 작업을 진행해서 원래 작업의 인덱스가 complete에 담겨 있음. 
    
    마지막은 complete에서 location의 인덱스를 추출하면 몇번째로 원하는 작업이 수행됐는지 알 수 있음
    단, .index 함수의 경우 0부터 시작하기 때문에 answer += 1 을 해줌. 

'''
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(x,y) for x,y in enumerate(priorities)])
    compare = deque(sorted(priorities, reverse = True))
    complete = []
    # 우선순위가 제일 높으면 꺼내고 아니면 rotate(-1)
    while queue:
        m = compare[0]

        if queue[0][1] == m:
            complete.append(queue.popleft()[0])
            compare.popleft()
            
        else:
            queue.rotate(-1)
        
    answer = complete.index(location) 
    
    # index이기 때문에 0부터 시작함 그래서 +1을 해서 리턴
    return answer+1