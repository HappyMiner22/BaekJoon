#입력은 여러 개의 테스트 케이스로 이루어져 있다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#각 테스트 케이스마다 A+B를 출력한다.
while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)

    except:
        break
