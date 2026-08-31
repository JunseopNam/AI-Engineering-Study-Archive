# cafe_order 카페 주문 영수증           -> 의문: list안에 list를 넣으면 더 코드가 이쁘지 않을까?

MENU = (('아메리카노', 4500), ('카페라떼', 5000), ('녹차', 4000))

divider1 = "=" * 30
divider2 = "-" * 30
divider3 = "=" * 34
divider4 = "-" * 34

print(divider1)
print(f'{"MENU":^26}')
print(divider1)
print(f'1. {MENU[0][0]:<12}' f'{MENU[0][1]:>8,}원')
print(f'2. {MENU[1][0]:<12}' f'{MENU[1][1]:>8,}원')
print(f'3. {MENU[2][0]:<12}' f'{MENU[2][1]:>8,}원')
print(divider1)


num = int(input("메뉴 번호: "))
qty = int(input("수량: "))
name, price = MENU[num - 1]

# print(name, price)

order_names = [name]
order_qtys = [qty]
order_amounts = [qty * price]

# print(order_names, order_qtys, order_amounts)


num2 = int(input("메뉴 번호: "))
qty2 = int(input("수량: "))
name2, price2 = MENU[num2 - 1]

order_names.append(name2)
order_qtys.append(qty2)
order_amounts.append(qty2 * price2)

# print(order_names, order_qtys, order_amounts)
# print(f"주문 항목 수: {len(order_names)}건")


total_amount = order_amounts[0] + order_amounts[1]
surtax = int(total_amount * 0.1)

print("\n" + divider3)
print(f"{'영수증':^26}")
print(divider3)
print(f"{order_names[0]:<12} {order_qtys[0]:>4}개 {order_amounts[0]:>11,}원")
print(f"{order_names[1]:<12} {order_qtys[1]:>4}개 {order_amounts[1]:>11,}원")
print(divider4)
print(f"{'주문 금액':<16} {total_amount:>13,}원")
print(f"{'부가세(10%)':<16} {surtax:>13,}원")
print(f"{'결제 금액':<16} {total_amount + surtax:>13,}원")
print(divider3)