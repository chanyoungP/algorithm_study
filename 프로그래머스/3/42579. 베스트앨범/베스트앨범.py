# idx 딕셔너리 {idx : [genres,plays]} 로 딕셔너리 만들고 
# genres 딕셔너리 {genres : genres합} 딕셔너리 만들고 
# 각 딕셔너리를 idx는 plays기준으로 정렬 
# genres는 genres 합 기준으로 정렬
# 정렬된 장르별로 for문을 돌면서 장르에 부합하는 idx를 answer.append 해주고 2개씩 append했으면 내부 for문 종료 
def solution(genres, plays):
    answer = []
    idx_dict = dict()
    genres_dict = dict()
    for i in range(len(genres)):
        idx_dict[i] = [genres[i],plays[i]]
        if genres[i] in genres_dict:
            genres_dict[genres[i]] += plays[i]
        else:
            genres_dict[genres[i]] = plays[i]
    sorted_genres_ = sorted(genres_dict.items(), key = lambda x : x[1],reverse = True)
    sorted_list = sorted(idx_dict.items(),key = lambda x : x[1][1],reverse = True)
    #sorted_list= [(idx,[genres,plays])] 
    # print(sorted_genres)
    sorted_genres = [k[0] for k in sorted_genres_]
    for gen in sorted_genres:
        count = 0
        for i in sorted_list:
            if i[1][0] == gen:
                answer.append(i[0])
                count += 1 
            if count == 2:
                break
    
    return answer