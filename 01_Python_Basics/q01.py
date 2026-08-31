# q01 변수는 값을 복사할까, 이름만 붙일까

a = [1, 2, 3]
b = a    # a랑 b가 같은 주소를 가르키게 된다
c = [1, 2, 3]

print(a is b, a is c, a == c)    # 예상출력: true, false, true
print(id(a) == id(b), id(a) == id(c))   # 예상출력: false, false -> 실재출력: true(주소가 완전 같음), false

b.append(4) # b에 4가 추가됨
print(a)    # 예상출력: 1, 2, 3, 4 -> 이유: a와 b는 같은 주소이기 때문에 b를 수정하면 a도 바뀌게 된다.
