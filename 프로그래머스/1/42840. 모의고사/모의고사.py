# 1번 1,2,3,4,5 1,2,3,4,5 
# 2번 2,1,2,3,2,4,2,5
# 3번 3,3,1,1,2,2,4,4,5,5,5 ,3,3 1,1,

# 정답 개수를 셀 리스트 생성 [0,0,0]
# 각 참가자의 정답지를 만들고 하나씩 비교? 
import collections
def solution(answers):
    answer = []
    i=1
    cnt = {1:0,2:0,3:0}
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for j in answers:
        # print(len(a)%i)
        # print(i%len(a))
        if a[i%len(a)-1] == j: # i%len(a)하면 1,2,3,4,0 여기서 -1 하면 0,1,2,3,-1로 
            cnt[1] += 1 # 알맞는 인덱스에 값을 불러올 수 있다. 
        if b[i%len(b)-1] == j:
            cnt[2] += 1
        if c[i%len(c)-1] == j:
            cnt[3] += 1
        i+=1 
    # cnt으로 하면 [0,0,0] 리스트에서 maximum value 여러 개 뽑아내는 방법?? 
    print(max(cnt.values()))
    for k,v in cnt.items():
        if v == max(cnt.values()):
            answer.append(k)
    return answer