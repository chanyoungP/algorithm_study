def solution(n, costs):
    # 비용이 낮은 순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # 각 섬이 속한 집합을 저장하는 배열
    parent = [i for i in range(n)]
    
    def find_set(x):
        if parent[x] != x:
            parent[x] = find_set(parent[x])
        return parent[x]
    
    def union_set(x, y):
        root_x = find_set(x)
        root_y = find_set(y)
        parent[root_y] = root_x
    
    answer = 0
    
    for cost in costs:
        island1, island2, bridge_cost = cost
        if find_set(island1) != find_set(island2):
            union_set(island1, island2)
            answer += bridge_cost
    
    return answer
