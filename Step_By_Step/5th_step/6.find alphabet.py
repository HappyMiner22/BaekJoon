#첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
#각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
#만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
#알파벳을 각각 비교해서 없는 것을 찾는 방법 뿐인가?

asciicode = 97
alphabet_list = []
for i in range(26):
    alphabet_list.append(chr(asciicode))
    asciicode += 1

character = input()
result = []

for j in range(26):
    if alphabet_list[j] in character:
        result.append(character.index(alphabet_list[j]))

    if alphabet_list[j] not in character:
        result.append(-1)

print(*result)