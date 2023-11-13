import collections
def solution(participant, completion):
    dic = collections.Counter(participant) # Counter 객체 생성 
    for name in completion: # 완주자 명단 순회
        if name in dic: # name이 참여자 명단에 있으면, 
            dic[name] -= 1 # value값 -= 1 
    # print(dic)
    print(dic.most_common(1))
    return dic.most_common(1)[0][0] #가장 큰 value를 가지고 있는 item 1개를 리턴jj