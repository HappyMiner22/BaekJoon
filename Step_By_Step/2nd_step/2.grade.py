#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

grade = int(input())

if grade <= 100 and grade >=90:
    print('A')
elif grade >=80 and grade <90:
    print('B')
elif grade >= 70 and grade <80:
    print('C')
elif grade >= 60 and grade <70:
    print('D')
else:
    print('F')