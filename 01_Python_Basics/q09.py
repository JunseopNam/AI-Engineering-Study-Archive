# q09 한 문장을 세 가지 방법으로

name = "홍길동"
age = 20
score = 92.5

print("%s님은 %i살이고 점수는 %0.1f점입니다." % (name, age, score))
print("{0}님은 {1}살이고 점수는 {2}점입니다.".format(name, age, score))
print(f"{name}님은 {age}살이고 점수는 {score}점입니다. ")