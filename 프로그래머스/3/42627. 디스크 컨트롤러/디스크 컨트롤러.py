import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now: #해당 프로세스의 요청시간이 start랑 now 사이 즉 이미 요청된 것
                # 즉 이미 요청된 프로세스라면, 힙에다가 [소요시간, 요청시간]으로 푸시를 해준다. 
                # 소요시간 기준으로 정렬된 힙이 필요하기 때문임.
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)