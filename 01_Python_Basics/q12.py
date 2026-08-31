# q12 영수증 만들기 (종합)

product = input()
price = int(input())
number = int(input())
total_price = price * number
surtax = int(total_price * 0.1)
divider1 = "=" * 38
divider2 = "-" * 38

print(divider1)
print(f'{"영수증":^38}')
print(divider1)
print(f'{product:<13}' + f"{number}개" + f'{total_price:>13,}')
print(divider2)
print("부가세(10%)" + f'{surtax:>13,}원')
print("합계" + f'{total_price + surtax:>15,}원')
print(divider1)