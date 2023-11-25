# 숫자를 조합한다.
    # permutations(numbers, 1~len(numbers))
    # list <- 조합들을 담고 
    # 중복 원소를 제거하기 위해서 set으로 변환
    # set의 원소들을 모두 숫자로 변환 
# 리스트를 돌면서 소수인지 확인한다. 
from itertools import permutations

def solution(numbers):
    
    #prime number인지 확인해주는 함수 -> prime이면 True 아니면 False 
    def is_prime(number):
        for i in range(2,number):
            if number%i == 0:
                return False
        return True
    
    answer = 0
    possible = list() # permutation 결과를 담을 리스트 
    candidate = [] # 조합을 숫자로 바꿔서 담을 리스트
    
    #numbers길이에 따라서 permutation 조합 수를 다 possible 리스트에 추가하는 루프
    for i in range(1,len(numbers)+1):
        possible += list(permutations(numbers,i))
    
    # possible에 있는 조합을 합친 문자열을 숫자로 만들어주는 루프
    for char in possible:
        s = ''.join(char) # Join()함수로 합치고 int로 만들어서 candidate에 append
        n = int(s)
        candidate.append(n)
    
    #중복된 숫자를 제거하기 위해서 set으로 만들어준다. 
    candidate = set(candidate)
    
    # is_prime을 활용해서 answer에 소수의 개수를 더해준다.
    for n in candidate:
        if is_prime(n) and n > 1:
            answer += 1 
                
    
    return answer