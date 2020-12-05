# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(bridge_length, weight, truck_weights):
    queue_time = []
    queue_weight = []
    time = 0
    while len(truck_weights) != 0:
        time += 1
        # trucks in bridge steps forward
        if len(queue_time) != 0:
            if time - queue_time[0] == bridge_length:
                del queue_time[0]
                del queue_weight[0]
        # add a truck to bridge
        if sum(queue_weight) + truck_weights[0] <= weight:
            queue_time.append(time)
            queue_weight.append(truck_weights[0])
            del truck_weights[0]
    # last truck go across the bridge
    time += bridge_length
    return time
