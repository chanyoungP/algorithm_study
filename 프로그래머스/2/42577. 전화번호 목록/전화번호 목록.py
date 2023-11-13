# 해시를 이용하려면, key = {번호 : [번호의 길이만큼 자른 나머지 번호들,]}
# key와 value 리스트의 값이 같은게 있으면 false 다르면 true 리턴? 

'''
아이디어 : 
- 딕셔너리 {number : len(number)} 생성
- 딕셔너리를 key값 기준으로 sorting하면, 전부 비교 안하고, 다음 번호만 비교할 수 있음. 
    - 사전식으로 정렬되서 가장 비슷한게 바로 옆에 오니까..
- sorting된 번호 쌍을 하나씩 비교하는데, 이전 번호의 길이만큼만 비교
- 같은게 있으면 False return 반복이 끝나면, True 리턴 
'''
def solution(phone_book):
    # answer = True
    dic = dict() # 딕셔너리 정의 
    for number in phone_book: # 딕셔너리 생성 
        dic[number] = len(number) # {번호 : 길이}
    sort_book = sorted(dic.items(), key = lambda x : x[0]) # key 기준 정렬
    
    for i in range(len(sort_book)-1): #정렬된 (번호 : 길이) 리스트 순회
        k,v = sort_book[i] # k,v를 따로 담아서 
        # print(sort_book[i+1][0][:v])
        if k == sort_book[i+1][0][:v]: # 현재 번호의 길이만큼만 비교
            return False
    return True