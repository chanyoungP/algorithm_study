'''
- [의상이름, 의상 종류] 가 주어질 때, 종류별로 1가지씩만 착용한다면, 서로 다른 의상의 조합의 수를 리턴

- {의상 종류 : 의상 수} 의 딕셔너리를 생성
- 키 별 의상 수 + 키 종류별 의상수 곱 리턴
'''
from functools import reduce
def solution(clothes):
    answer = 1
    dic = dict()
    for _, k in clothes:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    # print(dic.values())
    
    # 각 종류 원소의 합, 2종류고른 경우 (aa * bb + aa*cc + bb*cc) 3종류 고른 경우 (aa*b*c)
    # # n개의 종류 (2개 3개 4개 --- n개)
    # 종류 별로 a, b, c 개 있다고 하면 
    # a+b+c + ab + ac + bc + abc
    # (a+1)(b+1)(c+1)
    # (ab + a +b + 1)(c+1) = abc + ac + bc +c + ab + a + b + 1 
    #  = a + b + c + ac + bc + ab + abc + 1 
    for v in dic.values():
        answer *= (v+1)
    answer -= 1
    return answer