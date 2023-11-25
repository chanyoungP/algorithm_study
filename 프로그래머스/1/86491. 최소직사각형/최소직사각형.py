# 모든 명함을 수납할 수 있는 가장 작은 지갑
# 명함마다 돌면서 가로 세로의 최댓값을 갱신 -> 가로 세로를 돌려서도 생각을 해야함.
    # 가로 세로 돌렸을 때에도 크기가 크면, 큰 쪽을 갱신
    # max(x,y) 보다 max(w,h)가 더 크면, 갱신 
    # min(x,y) 보다 min(w,h)가 더 크면, 갱신 
def solution(sizes):
    answer = 0
    m_w = 0
    m_h = 0
    for w,h in sizes:
        print(m_w,m_h)
        if max(m_w,m_h) < max(w,h):
            m_w = max(w,h)
        if min(m_w,m_h) < min(w,h):
            m_h = min(w,h)
    print(m_w,m_h)

    return m_w*m_h