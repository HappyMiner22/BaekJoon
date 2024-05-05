#책에는 long int는
#4바이트 정수까지 저장할 수 있는 정수 자료형이고 long long int는 8바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다.
#혜아는 이런 생각이 들었다. “int 앞에 long을 하나씩 더 붙일 때마다 4바이트씩 저장할 수 있는 공간이 늘어나는 걸까?
#첫 번째 줄에는 문제의 정수 N주어짐
#혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

ask = int(input())

answer = 'int'

for i in range(ask // 4):
    answer = 'long ' + answer

print(answer)