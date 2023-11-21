def solution(operations):
    answer = []
    q = [] # q 리스트를 하나 생성
    for op in operations: # operations를 순회하면서 
        q.sort() #처음 q를 sorting 
        print(q)
        s,v = op.split(" ") #op -> op number 로 되어 있으니까 나눠서 할당
        v = int(v) # string -> int로 변환 
        if s =="I":
            q.append(v)
        elif s == "D" and len(q) > 0:
            if v == 1: # D이고 1이면 최댓값을 삭제
                q.pop()
            else: # D 이고 -1이면 최솟값을 삭제 
                q.pop(0)
    if len(q) == 0: # 모든 명령을 수행하고 q가 비어있으면 0,0 을 리턴
        answer = [0,0]
    else: # 아닌 경우에는 max min 값을 리턴 
        answer = [max(q),min(q)]

            
                
    return answer