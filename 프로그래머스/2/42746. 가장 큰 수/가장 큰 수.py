def solution(numbers):
    ### 검색 참고 ###
    numbers = list(map(str, numbers)) # numbers를 str로 바꿔서 리스트를 생성
    numbers.sort(key=lambda x: x*3, reverse=True) 
    # x*3 -> [1,2,3] -> [111,222,333] #문자열 비교를 아스키 코드로 하는데, 자릿수를 맞춰서 비교하기 위함. 
    return str(int(''.join(numbers)))