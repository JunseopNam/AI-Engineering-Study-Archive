# q06 문장 분석하기

s = "  Life is too short, You need Python  "
no_empty_s = s.lstrip().rstrip()

print(len(s), len(no_empty_s))
print(no_empty_s.count('o'))
print(no_empty_s.find('short'), no_empty_s.find('Java'))
print(no_empty_s.replace('Python', 'Java'))
print(no_empty_s.split(), '\n' + str(len(no_empty_s.split())))