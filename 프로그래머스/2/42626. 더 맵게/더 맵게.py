'''
질문하기 봄... 
'''

import heapq as hp # 파이썬 heap 라이브러리 

def solution(scoville, K):
    hp.heapify(scoville)    # scoville 리스트를 힙 자료형으로 만들기
    
    count = 0
    while scoville[0] < K : # 인덱스 0이 제일 최소값이기 때문에 0만 검사하면 되는거
        count += 1
        
        min_one = hp.heappop(scoville)  #pop해도 heap 모듈이 알아서 정렬해줌,
        min_two = hp.heappop(scoville)  #그래서 정렬을 다시 할 필요 없이 두번째로 작은 값을 추출할 수 있다.
        hp.heappush(scoville, min_one + min_two*2)# push 역시 마찬가지 
        
        # 모든 스코빌을 K 이상으로 만들 수 없는 경우
        if (len(scoville) == 2) and (scoville[0] + scoville[1]*2) < K: 
            return -1  
        
    return count