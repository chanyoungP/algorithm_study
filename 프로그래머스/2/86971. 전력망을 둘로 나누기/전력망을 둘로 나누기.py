from collections import deque

def bfs(start,visitied,graph): #        visitied = [False]*(n+1)
    queue = deque([start])
    result = 1
    visitied[start] = True
    
    while queue:
        now = queue.popleft() 
        
        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                queue.append(i)
                visitied[i] = True
                
    return result
        

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)] # [[] [] [] []] 인 그래프 구조를 생성
    print(graph)
    for v1,v2 in wires: # 와이어에서 graph v1과 v2자리에 각각 삽입
        graph[v1].append(v2) # v1노드에 v2노드 연결
        graph[v2].append(v1)  # v2노드에 v1노드 연결 
        # 인덱스 : 해당 노드 번호, #각 노드에 연결되어 있는 노드번호가 들어감.
        # [[],[3],[3],[1,2,4]] : 1번 노드는 3번과 연결, 2번 노드 .. 3번 노드는 1,2,4번과 
    print(graph)
    for start,not_visit in wires: # 연결 하나씩 돌면서 
        visitied = [False]*(n+1) # 전부 False 처리로 초기화 case별로 해야하니까 여기서 
        visitied[not_visit] = True # 간선 자르기 
        result = bfs(start,visitied,graph) #bfs 진행
        if abs(result - (n-result)) < answer: # 최솟값으로 업데이트 
            answer = abs(result - (n-result))
        
    return answer