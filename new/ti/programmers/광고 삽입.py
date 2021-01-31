# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(play_time, adv_time, logs):
    indexes = []
    for log in logs:
        log_split1 = log.split('-')
        index = []
        for _log_split1 in log_split1:
            log_split2 = _log_split1.split(':')
            index.append(int(log_split2[0]) * 3600 + int(log_split2[1]) * 60 + int(log_split2[2]))
        indexes.append(index)
    adv_split = adv_time.split(":")
    adv_len = int(adv_split[0]) * 3600 + int(adv_split[1]) * 60 + int(adv_split[2])
    end_split = play_time.split(":")
    end_time = int(end_split[0]) * 3600 + int(end_split[1]) * 60 + int(end_split[2])
    #     indexes:list, adv_len:int end_time:int
    plays = [0 for _ in range(end_time)]
    dict_indexes = {}
    for index in indexes:
        if index[0] in dict_indexes:
            dict_indexes[index[0]] = dict_indexes[index[0]] + 1
        else:
            dict_indexes[index[0]] = 1
        if index[1] in dict_indexes:
            dict_indexes[index[1]] = dict_indexes[index[1]] - 1
        else:
            dict_indexes[index[1]] = -1
    dict_indexes = sorted(dict_indexes.items(), key=lambda x: x[0])
    # print(dict_indexes)?
    plays = []
    head = 0
    user = 0
    for dict_index in dict_indexes:
        plays += [user for _ in range(dict_index[0] - head)]
        head = dict_index[0]
        user += dict_index[1]
    plays += [user for _ in range(end_time - head)]
    start = 0
    end = adv_len - 1
    answer_int = 0
    current_play_time = sum(plays[start:end + 1])
    max_play_time = current_play_time
    # answer_int, current_play_time, max_play_time, plays[], start, end
    while end < end_time - 1:
        current_play_time -= plays[start]
        start += 1
        end += 1
        current_play_time += plays[end]
        if max_play_time < current_play_time:
            answer_int = start
            max_play_time = current_play_time
    hours = str(answer_int // 3600)
    if len(hours) == 1:
        hours = '0' + hours
    minutes = str((answer_int % 3600) // 60)
    if len(minutes) == 1:
        minutes = '0' + minutes
    seconds = str((answer_int % 3600) % 60)
    if len(seconds) == 1:
        seconds = '0' + seconds
    answer = hours + ':' + minutes + ':' + seconds
    return answer
