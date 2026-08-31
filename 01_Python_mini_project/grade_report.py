# grade_report 우리반 성적 리포트

SUBJECT = ('국어', '영어', '수학')

names = ['김민준', '이서연', '박도윤']
scores = [88, 95, 76]

### Step1 print
# print("과목:", SUBJECT)
# print(f"등록된 학생: {len(SUBJECT)}명")
# print(f'첫 번째 학생: {names[0]} / {scores[0]}점')
# print(f'마지막 학생: {names[-1]} / {scores[-1]}점')

names.append(input("추가할 학생 이름: "))
scores.append(int(input("점수: ")))

### Step2 print
# print(names)
# print(scores)
# print(f"이제 {len(scores)}명 입니다.")

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

### Step3 print
# print(f"총점: {total}점")
# print(f"평균: {average:2.1f}점")
# print(f"최고점: {highest}점 / 최저점: {lowest}점")

top_index = scores.index(highest)
top_name = names[top_index]
find_index = names.index('박도윤')

### Step4 print
# print(f"1등: {names[top_index]} ({highest}점) - scores[{top_index}]자리")
# print(f"박도윤의 점수: {scores[find_index]}점 (names[{find_index}])")
# print("점수 내림차순:", sorted(scores, reverse=True))
# print("이름 가나다순:", sorted(names))

divider1 = "=" * 30
divider2 = "-" * 30

print(divider1)
print(f'{"성적리포트":^25}')
print(divider1)
print(f"{'이름':<12} {'점수':>8}")
print(divider2)
print(f"{names[0]:<12} {scores[0]:>8}")
print(f"{names[1]:<12} {scores[1]:>8}")
print(f"{names[2]:<12} {scores[2]:>8}")
print(f"{names[3]:<12} {scores[3]:>8}")
print(divider2)
print(f"{'평균':<12} {average:>8.1f}")
print(f"{'1등':<12} {top_name:>8}")
print(divider1)


### 도전과제1 - 최저점 학생 내보내기
i = scores.index(min(scores))

print(f"\n제외: {names.pop(i)}({scores.pop(i)}점)")


### 도전과제2 - 전학생 맨 앞에 넣기
names.insert(0,'한지민')
scores.insert(0, 100)
average = sum(scores) / len(scores)

print(f"새로운 평균점수: {average:0.1f}점")


### 도전과제3 - 동점자 확인하기
print(scores.count(92))