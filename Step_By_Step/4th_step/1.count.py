#첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
#둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
#첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

#변수를 여러 번 선언할 수 있나? 음.... -> list()함수로 해결! // 입력받은 값을 list로 변환해주면 끝임.
wtf = int(input())
a = list(map(int, input().split()))

b = int(input())

result = a.count(b)
print(result)