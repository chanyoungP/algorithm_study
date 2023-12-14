def solution(number, k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 남은 k개의 수를 뒤에서 제거
    stack = stack[:-k] if k > 0 else stack
    
    answer = ''.join(stack)
    return answer
