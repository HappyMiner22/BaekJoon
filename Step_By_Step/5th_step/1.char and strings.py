#첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 S가 주어진다. 단어의 길이는 최대 1\,000이다.둘째 줄에 정수 i가 주어진다.
#S의 i번째 글자를 출력한다.

ask_character = input()
find_charcter = int(input())
listed = list(ask_character)
result = ask_character[find_charcter-1]
print(result)
