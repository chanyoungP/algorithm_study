# 단어가 주어지면 사전에서 몇번째에 위치해있는지 리턴
# 사전 순은 A E I O U 이고 길이는 5이하 마지막 단어는 UUUUU 
# A AA AAA AAAA AAAAA 순으로 
# 풀이 
# 단어로 모든 단어 만들어서 해당하는 인덱스 찾기 
# permutation 중복 가능? --> product() 함수 
# product() -> product(A, B) returns the same as ((x,y) for x in A for y in B).
from itertools import product
def solution(word):
    answer = 0
    total = [] # product로 만들 튜플을 담을 리스트 
    words = [] # 단어로 만들어서 담을 리스트
    
    #단어 제한이 1자리 부터 5자리니까 그에 해당하는 반복을 모두 해줘야함. 
    for i in range(1,6):
        total += list(product('AEIOU',repeat=i))
    
    # total에서 하나씩 가져와서 ('A','A','E') -> 'AAE'로 바꾸는 과정
    for s in total:
        words.append(''.join(s))
    
    # 문자열을 사전 순으로 정렬하면 문제에서 원하는 순서로 정렬 
    sorted_words = sorted(words)
    
    # for i in range(6):
    #     print(sorted_words[i])
    
    #해당하는 문자 word의 인덱스를 sorted_words에서 찾고 +1 해주면 정답
    answer = sorted_words.index(word) + 1 
    
    
    return answer