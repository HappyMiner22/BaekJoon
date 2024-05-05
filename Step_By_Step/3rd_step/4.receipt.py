#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
#첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다. 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다. 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

price = int(input())

product_quantity = int(input())

total_price = 0
for i in range(product_quantity):
    a, b = map(int, input().split())
    each_product_price = a
    each_product_quantity = b
    sumed_up = each_product_quantity * each_product_price #여기서 모르겠는거: 이 줄의 변수가 루프를 돌 때마다 초기화되는데 이 초기화를 저장하고 싶음.
    total_price += sumed_up

if total_price == price:
    print("Yes")

else:
    print("No")
