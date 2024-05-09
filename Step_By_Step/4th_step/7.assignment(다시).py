#입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
#출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

"""students = []
for i in range(28):
    ask = int(input())
    students.append(ask)

students.sort()
for j in range(1, 29):
    find = students.index(j)
    if find == 0:
        print(find)
"""

student = []

for i in range(30):
    student.append(False)

for i in range(28):
    a = int(input())
    student[a - 1] = True

for i in range(30):
    if student[i] == False:
        print(i + 1)
