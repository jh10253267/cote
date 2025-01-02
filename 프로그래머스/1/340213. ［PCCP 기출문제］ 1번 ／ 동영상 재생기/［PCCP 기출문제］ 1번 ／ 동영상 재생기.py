from datetime import timedelta
# 오프닝 구간이라면 오프닝이 끝나는 구간으로 이동

def solution(video_len, pos, op_start, op_end, commands):
    delta = timedelta(seconds=10)
    pos = time_converter(pos)
    start = time_converter("00:00")
    op_start = time_converter(op_start)
    op_end = time_converter(op_end)
    end = time_converter(video_len)
    
    for command in commands:
        if op_start <= pos and pos <= op_end:
            pos = op_end
        if command == "next":
            if op_start <= pos+delta and pos+delta <= op_end:
                pos = op_end
            else:
                pos = min(pos + delta, end)
        else:
            if op_start <= pos - delta and pos - delta <= op_end:
                pos = op_end
            else:
                pos = max(pos - delta, start)
        
    return str(pos)[2:]

def time_converter(str_time):
    minutes, second = map(int, str_time.split(":"))
    time_delta = timedelta(minutes=minutes, seconds=second)
    return time_delta