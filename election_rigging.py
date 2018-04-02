"""
    1. 다솜이는 각 사람들이 누구를 찍을지 알고있다.
    2. 국회의원의 후보수는 n 명이다
    3. 다솜이는 기호 1번이다.
    4. 다솜이는 자신이 당선이 되기위해 자신을 찍지않으려는 사람들을 매수한다.
    5. 다솜이가 매수해야하는 사람의 최소값을 구하자.
"""

n = int(input())  # 후보의 수
input_voters = []  # 후보의 지지자수

for i in range(n):  # 후보의 수만큼 입력받기
    input_voters.append(int(input()))


def buyer_counting(dasom, voters, buyer):
    if len(voters) == 0:  # 후보자가 다솜 1명이라면
        return 0   # 0 리턴

    if dasom > max(voters):  # 다솜후보의 지지자가 다른 후보의 지지자수 보다 클경우
        return buyer  # 매수한 지지자수 리턴
    else:  # 아니라면
        voters[voters.index(max(voters))] -= 1  # 다른 후보자들의 지지자수중 가장 많은 지지자수를 1명씩 매수
        buyer += 1  # 매수한 지지자수 증가
        dasom += 1  # 다솜의 지지자수 증가

        return buyer_counting(dasom, voters, buyer)  # 재귀함수 호출


print(buyer_counting(dasom=input_voters.pop(0), voters=input_voters, buyer=0))


