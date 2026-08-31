# course 수강신청 명단 분석기

divider1 = "=" * 32
divider2 = "-" * 32

phython_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민']

phython_set = set(phython_list)
web_set = set(web_list)

# step 1
print(f"파이썬 신청 {len(phython_list)}건 -> 실재 {len(phython_set)}명")
print(f"웹개발 신청 {len(web_list)}건 -> 실재 {len(web_set)}명")
print(sorted(phython_set))
print(sorted(web_set))

# step 2
both = phython_set & web_set
all_students = phython_set | web_set
only_python = phython_set
only_web = web_set
one_only = phython_set ^ web_set

print(f"둘 다 수강: {sorted(both)}")
print(f"전체 수강생: {sorted(all_students)}")
print(f"파이썬만: {sorted(only_python)}")
print(f"웹개발만: {sorted(only_web)}")
print(f"한과목만: {sorted(one_only)}")

# step 3
name = '이서연'

print(f"이서연 파이썬 수강? {name in phython_set}")
print(f"이서연 웹개발 수강? {name in web_set}")
print(f"이서연 둘 다 수강? {name in both}")
print(f"이서연 하나라도 수강? {name in all_students}")
print(f"이서연 미수강? {name not in all_students}")
print(f"교집합이 비었나? {not bool(both)}")

# step 4
report = {'python':len(only_python), 'web':len(only_web), 'both':len(both), 'total':len(all_students)}

print(report)
print(divider1)
print(f"{'수 강 현 황':^16}")
print(divider1)
print(f"{'과목별 인원':<14} {len(only_python):>10}명")
print(f"{'웹개발':<14} {len(only_web):>10}명")
print(divider2)
print(f"{'둘다 수강':<14} {len(both):>10}명")
print(f"{'전체 인원':<14} {len(all_students):>10}명")
print(divider1)
print(f"{'중복 수강률':<14} {(len(both) / len(all_students) * 100):>10.1f}%")
