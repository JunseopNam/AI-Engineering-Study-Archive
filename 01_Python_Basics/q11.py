# q11 나이 계산기

name = input("이름을 입력하세요: ")
birth_year = int(input("태어난 해를 입력하세요: "))

print(type(name), type(birth_year))
print(f'{name}님은 올해 {2026 - birth_year}살 입니다')
print(f'{name}님은 내년이면 {2026 - birth_year + 1}살이 됩니다.')