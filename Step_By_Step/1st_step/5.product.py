#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#문제 제대로 읽기!!!!!!!!!!!!!!!!!!!
first = int(input())
second = int(input())

second_unit = second % 10
second_tenth = (second // 10) % 10
second_hunnid = second // 100

three = first * second_unit
fo = first * second_tenth
fi = first * second_hunnid
si = first * second

print(three)
print(fo)
print(fi)
print(si)
