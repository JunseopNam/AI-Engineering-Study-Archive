# q10 줄 맞춰 표 출력하기

contour = "-" * 38

apple = "사과"
apple_count = 3
apple_unit_price = 1500
apple_whole_price = apple_count * apple_unit_price

banana = "바나나"
banana_count = 12
banana_unit_price = 800
banana_whole_price = banana_count * banana_unit_price

water_melon = "수박"
water_melon_count = 1
water_melon_unit_price = 22000
water_melon_whole_price = water_melon_count * water_melon_unit_price


print(f'{"상품명":<8}' + f'{"수량":<7}' + f'{"단가":<7}' + f'{"금액":<7}')
print(contour)
print(f'{apple:<10}' + f'{apple_count:<7}' + f'{apple_unit_price:<7,}' + f'{apple_whole_price:<7,}')
print(f'{banana:<10}' + f'{banana_count:<7}' + f'{banana_unit_price:<7,}' + f'{banana_whole_price:<7,}')
print(f'{water_melon:<10}' + f'{water_melon_count:<7}' + f'{water_melon_unit_price:<7,}' + f'{water_melon_whole_price:<7,}')
print(contour)
print(f'{"합계":<24}' + f'{apple_whole_price + banana_whole_price + water_melon_whole_price:<7,}')