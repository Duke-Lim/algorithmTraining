"""
    1. 물품은 연속되게 3개씩 묶을수있다.
    2. 묶은 물품중 가장 싼 것은 무료로 지급한다.
    3. 모든 상품을 구매한다고 했을때 필요한 최소 금액을 구하자.
"""

n = [8, 3, 5, 2, 3, 5, 7]  # 물품과 그 가격

array = []  # 3개씩 묶었을때 가장 적은 가격과 그 묶은 물품을 저장하는 리스트

for i in range(len(n)):  # 물품의 개수만큼 반복
    temp_tuple = (n[i], n[i+1], n[i+2])  # 리스트의 0번째 부터 3개씩 묶기

    array.append((min(temp_tuple), temp_tuple))  # 가장 적은 가격과 그 묶은 물품을 (3, (8, 3, 5) 형태로 저장

    if n[i+2] == n[-1]:  # 3개씩 다 묶었다면
        break  # 반복문 종료

array.sort(reverse=True)  # 가장 할인이큰 물품으로 정렬

price_sum = 0  # 최종 금액

for i in range(len(n)//3):  # 최대 묶을수 있는 개수 만큼 반복
    price_sum += sum(array[i][1]) - array[i][0]  # 가장 적은 가격을 뺀 물품의 가격을 더한다.
    for j in range(len(array[i][1])):  # 할인 받을 물품의 개수만큼 반복
        n.remove(array[i][1][j])  # 물품의 리스트에서 더한 물품은 삭제

price_sum += sum(n)  # 나머지 할인받지 못한 물품의 가격을 더한다.

print(price_sum)
