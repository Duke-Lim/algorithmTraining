"""
    1. 입력받은 숫자를 2진수로 변환한다.
    2. 그뒤 첫번째 맵과 두번째 맵을 합친다.
    3. 합친맵에서 1이상인 수는 #으로하고 0이면 빈공간으로한다.

    정답률 : 81.78%
"""


def convert(n):  # 2진법으로 변환하는 함수
    T = "0123456789ABCDEF"
    q, r = divmod(n, 2)
    if q == 0:
        return T[r]
    else:
        return convert(q) + T[r]


n = int(input())

array1 = []
array2 = []
array3 = []
result = []

for i in range(n):
    array1.append(int(input()))

for i in range(n):
    array2.append(int(input()))

for i in range(n):
    a = int(convert(array1[i]))
    b = int(convert(array2[i]))

    array3.append(a+b)

    map = ""

    for j in range(n):
        s = str(array3[i])

        if s[j] == "0":
            map += " "
        else:
            map += "#"

    result.append(map)

for i in range(len(result)):
    print(result[i])
