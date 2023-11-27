from itertools import permutations
# 가능한 던전 탐험 경우의 수 모두를 구해서 최대한 많은 경우를 리턴
# 가능한 경우의 수 만들기
    # permutations 함수 이용해서 던전 수 만큼 경우의 수 생성 
    # permutations(range(len(dungenons)),len(dungeons))
# 가능한 경우의 수별로 던전 탐험 진행
    # 던전 돌기전에 최소 피로도 체크
    # 돌고 나서 피로도 마이너스 count +1 
def solution(k, dungeons):
    answer = []
    permu = list(permutations(range(len(dungeons)),len(dungeons)))
    # print(permu)
    for case in permu:
        cnt = 0 # case 마다 카운트 해야하니까 여기서 초기화
        stat = k
        for i in case:
            if dungeons[i][0] <= stat: # 던전 입장 가능
                cnt += 1
                stat -= dungeons[i][1]
        # case 하나 끝나면, 해당 case의 던전 탐험 횟수를 리스트에 담는다.
        answer.append(cnt)
    # print(answer)
    return max(answer)