# q07 이메일 주소 분해하기

email = "hong.gildong@example.com"
name = email[:12]
domain =  email[13:]

print(email.find('@'))

print(name, domain)
#print(email.split('@'))

print(name.upper(), domain[:7])