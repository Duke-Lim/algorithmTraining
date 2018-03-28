"""
    1. 버스는 09:00 시부터 시작한다.
    2. 버스는 도착한 순간에 대기 순서대로 태운 후 바로 출발한다.
    3. 콘은 같은 시각에 도착한 사람 중 제일 뒤에 선다.
    4. 모든 사람은 23:59에는 모두 집으로 돌아간다. 즉, 다음날 버스를 타는 경우는 없다.
    5. 콘이 버스를 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하자.
    5-1. 버스의 정원이 남는 경우 콘은 버스 도착 시각에 맞춰 정류장에 가면 된다.
    5-2. 버스의 정원이 남지 않는 경우 콘은 마지막에 버스에 타는 사람보다 1분 일찍 정류장에 가면 된다.

    정답률 : 26.79%
"""


def list_to_minute(list):  # 리스트의 시간을 분으로 바꿔주는 함수
    result = []

    for i in list:
        hour = int(i[0:2])
        minute = int(i[3:5])

        result.append(hour * 60 + minute)

    return result


def minute_to_time(minute):  # 분을 시간으로 바꿔주는 함수
    hour = int(minute / 60)
    minute = minute % 60
    result = ""

    if hour < 10:
        result += "0" + str(hour)
    else:
        result += str(hour)

    result += ":"

    if minute < 10:
        result += "0" + str(minute)
    else:
        result += str(minute)

    return result


n = 2  # 버스의 운행 횟수
t = 10  # 버스의 운행 시각 간격
m = 2  # 한 버스에 탈 수 있는 최대 인원
timetable = ["09:10", "09:09", "08:00"]  # 버스를 타는 사람의 대기열
timetable.sort()  # 대기열을 오름차순으로 정렬
convert_timetable = list_to_minute(timetable)  # 리스트를 분으로 변경

checkCrew = 0  # 버스에 탄 사람 수
busTime = 540  # 버스의 도착시각 첫차는 09:00 시
conTime = 0  # 콘이 버스를 탈 시각

for i in range(n):
    seat = m  # 운행 시간마다 버스에 탈 수 있는 최대 인원의 수
    j = checkCrew

    for j in range(len(convert_timetable)):
        if convert_timetable[j] <= busTime:
            seat = seat - 1
            checkCrew = checkCrew + 1
            if seat == 0:  # 자리가 없다면 탑승 종료
                break

    if i == n-1:  # 버스의다음 운행이 없으면 즉, 막차라면
        if seat == 0:
            conTime = convert_timetable[checkCrew - 1] - 1
        else:
            conTime = busTime

    busTime += t
    if busTime > 60*24:
        break

print(minute_to_time(conTime))
