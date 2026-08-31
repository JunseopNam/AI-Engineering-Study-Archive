# profile 학생 프로필 카드

student = {'name':'김민준', 'age':20, 'major': '컴퓨터공학'}
divider1 = "=" * 34
divider2 = "-" * 34

# step 1
print(student)
print(student['name'], student['age'], student['major'], )
print(f'학생 수: {len(student)}개 항목')

# step 2
student['email'] = 'minjun@example.com'
student['hobbies'] = ['python', 'game']
student['age'] = 21
del student['major']

print(student)
print(f'항목 수: {len(student)}')

# step 3
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', '등록되지 않음'))
print('email' in student, 'major' in student)

# step 4
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))


# step 5
print(divider1)
print(f"{'P R O F I L E':^30}")
print(divider1)
print(f"{'이름':<12}{student.get('name'):>18}")
print(f"{'나이':<12}{student.get('age'):>18}")
print(f"{'이메일':<12}{student.get('email'):>18}")
print(f"{'전화':<12}{student.get('phone', '미등록'):>18}")
print(divider2)
print(f"{'취미':<12}{str(student['hobbies']):>18}")
print(f"{'항목 수':<12}{len(student):>18}")
print(divider1)