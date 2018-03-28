s = input()
n = int(input())
result = ""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for str in s:
    change = alphabet.find(str)+n

    if change >= 26:
        change = change - 26

    result += alphabet[change]

print(s)
print(result)