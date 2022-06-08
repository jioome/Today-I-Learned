import math


def solution(m, musicinfos):
    answer = None
    # 문자열 치환
    m = m.replace("C#", "c").replace("D#", "d").replace(
        "F#", "f").replace("G#", "g").replace("A#", "a")

    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")

        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start  # 음악이 play된 시간

        # 악보 # 제거
        code = code.replace("C#", "c").replace("D#", "d").replace(
            "F#", "f").replace("G#", "g").replace("A#", "a")

        if len(code) > duration:
            code = code[:duration]
        else:
            q, r = divmod(duration, len(code))
            code = code*q + code[:r]

        if m not in code:
            continue

        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
            answer = (duration, start, title)

    if answer:
        return answer[-1]

    return "(None)"
