import collections

def solution(nums):
    dic = collections.Counter(nums)
    get_ = int(len(nums)/2)
    print(dic)
    return min(len(dic),get_)