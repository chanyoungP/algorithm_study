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
            if v == 1:
                q.pop()
            else:
                q.pop(0)
    if len(q) == 0:
        answer = [0,0]
    else:
        answer = [max(q),min(q)]

            
                
    return answer