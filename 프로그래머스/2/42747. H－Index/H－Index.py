'''어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.'''
# h번 이상 인용된 논문이 h편 이상
# 크기 순으로 정렬해서 [0,1,3,5,6] for i in range(1,len(citations)+1):
    # case i == 1 , k = i이상인 원소의 개수 if i==k , break 
    # i이상인 원소의 수를 세는 방법  : len(list(filter(lambda x : x >= i , citations)))
def solution(citations):
    answer = 0
    r = []
    for i in range(1,len(citations)+1):
        k = len(list(filter(lambda x : x >= i, citations)))
        if i <= k:
            answer = i
    
    return answer