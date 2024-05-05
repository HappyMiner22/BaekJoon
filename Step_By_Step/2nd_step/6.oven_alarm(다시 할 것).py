#첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
#두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
#첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

'''h, m = map(int, input().split())
consuming_time = int(input())

if m + consuming_time > 60:
    remainder = 60 - (m + consuming_time)
    if remainder <0:
        remainder = abs(remainder)

    m = 0
    m += remainder
    h+=1
    if h == 24:
        h = 0
    print(f'{h} {m}')

elif m + consuming_time == 60:
    m = 0
    h += 1
    if h == 24:
        h = 0
    print(f'{h} {m}')

else:
    timenow = m + consuming_time
    if h == 24:
        h = 0
    print(f'{h} {timenow}')'''

'''h, m = map(int, input().split())
consuming_time = int(input())

# 총 소요 시간을 분으로 환산
total_minutes = h * 60 + m + consuming_time

# 시간과 분을 다시 계산
new_h = total_minutes // 60 % 24
new_m = total_minutes % 60

print(f'{new_h} {new_m}')'''