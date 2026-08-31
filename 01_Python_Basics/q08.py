# q08 개인정보 가리기

jumin = "990101-1234567"
card = "1234-5678-9012-3456"
secure_jumin = jumin[:-6] + '*' * 6
secure_card = '*' * 14 + card[-4:]

print(secure_jumin)
print(len(secure_jumin))
print(secure_card)
