def solution(scores):
    answer = ''
    for i in range(len(scores)):
        i_scores = [scores[j][i] for j in range(len(scores))]
        ## 유일한 최고점 또는 최저점 제거
        if i_scores[i] in (min(i_scores), max(i_scores)) and i_scores.count(i_scores[i]) == 1:
            del i_scores[i]
        # 학점 구하기
        avg = sum(i_scores) / len(i_scores)
        if 90 <= avg:
            answer += 'A'
        elif 80 <= avg < 90:
            answer += 'B'
        elif 70 <= avg < 80:
            answer += 'C'
        elif 50 <= avg < 70:
            answer += 'D'
        else:
            answer += 'F'
    return answer
