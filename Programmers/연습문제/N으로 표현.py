def solution(N, number):
    # 집합을 원소로 하는 배열 생성 / 중복되는 값이 발생하므로 집합 사용 / 'N', 'NN', 'NNN' ... 값을 포함해서 초기화
    dp = [{}] + [{int(str(N) * i)} for i in range(1, 9)]
    # i + j <= 8 을 만족하는 i, j에 대해서 이중 for문 수행
    for i in range(1, 9):
        for j in range(i, 9 - i):
            # 두 집합 각각의 모든 원소들에 대해서 연산 수행
            for op1 in dp[i]:
                for op2 in dp[j]:
                    # 두 연산자에 대해 가능한 모든 사칙 연산
                    dp[i + j].add(op1 + op2)
                    dp[i + j].add(op1 - op2)
                    dp[i + j].add(op2 - op1)
                    dp[i + j].add(op1 * op2)
                    # 나누는 수가 0인 경우를 고려
                    if op2 != 0:
                        dp[i + j].add(op1 // op2)
                    if op1 != 0:
                        dp[i + j].add(op2 // op1)
    # 1 ~ 8까지 순회하며 찾는 숫자가 존재할 경우 인덱스 반환
    for i in range(1, 9):
        if number in dp[i]:
            return i
    # 최솟값이 8보다 클 경우 -1 반환
    return -1
