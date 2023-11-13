# 아이디어 
# "(" 가 나오면 stack에 push하고 ")"가 나오면 stack에서 pop을 해서 
# 마지막에 stack이 비어있으면 true 아니면 false
# stack이 비어있는데 ")" 나오면 false 리턴 
def solution(s):
    answer = True
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif not stack and char == ")":
            return False
        elif stack and char == ")":
            stack.pop()
    return True if not stack else False