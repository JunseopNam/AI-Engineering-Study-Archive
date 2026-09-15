# supervised_learning 1.regression and 2.classification

"""
상황. 환자 한 명의 정보 10가지가 주어졌을 때, 1년 뒤 진행도 점수가 몇 점일지 맞히는 프로그램을 만드세요. 
정답이 25.0부터 346.0까지의 숫자이므로 회귀 문제입니다

1단계 - 데이터를 불러오고 학습용 8 : 시험용 2로 나눈다
2단계 - LinearRegression 모델을 만들고 학습용 데이터로 학습시킨다
3단계 - 시험용 입력을 넣어 점수를 예측한다
4단계 - 예측이 정답에서 얼마나 빗나갔는지 채점한다
5단계 - 기준 모델과 비교해 잘한 것인지 판단한다
"""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1단계 - 데이터 불러오고 나누기
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2단계 - 모델을 만들고 학습시키기
model = LinearRegression()
model.fit(X_train, y_train)             # TODO

# 3단계 - 시험용 데이터로 예측하기
pred = model.predict(X_test)              # TODO

# 4단계 - 채점하기
print("평균오차 = %6.2f" % mean_absolute_error(y_test, pred))               # TODO
print("설명력 = %7.4f" % r2_score(y_test, pred))                # TODO

# 5단계 - 기준 모델과 비교하기
base = DummyRegressor(strategy="mean")
# TODO: base를 학습시키고 예측한 뒤, 4단계와 같은 방식으로 채점하세요
base.fit(X_train, y_train)
base_pred = base.predict(X_test)
print("기준 모델 평균오차 = %6.2f" % mean_absolute_error(y_test, base_pred))
print("기준 모델 설명력 = %7.4f" % r2_score(y_test, base_pred))



from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, confusion_matrix)

# 1단계 - 숫자 정답을 예/아니오 정답으로 바꾸기
y_train_c = (y_train > 140).astype(int)    # 140점 넘으면 1
y_test_c = (y_test > 140).astype(int)

# 2단계 - 모델을 만들고 학습시키기
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train_c)    # TODO: 정답 자리에 무엇을 넣어야 할까요?

# 3단계 - 시험용 데이터로 예측하기
pred = clf.predict(X_test)    # TODO

# 4단계 - 채점하기
print("정확도 = %.4f" % accuracy_score(y_test_c, pred))    # TODO
# TODO: 정밀도, 재현율, 네 칸짜리 표도 같은 방식으로 출력하세요
print("정밀도 = %.4f" % precision_score(y_test_c, pred))
print("재현율 = %.4f" % recall_score(y_test_c, pred))
print("네 칸짜리 표:\n", confusion_matrix(y_test_c, pred))

# 5단계 - 기준 모델과 비교하기
base = DummyClassifier(strategy="most_frequent")
# TODO: base를 학습시키고 정확도를 구해 내 모델과 비교하세요
base.fit(X_train, y_train_c)
base_pred = base.predict(X_test)
print("정확도 = %.4f" % accuracy_score(y_test_c, base_pred))
print("정밀도 = %.4f" % precision_score(y_test_c, base_pred))
print("재현율 = %.4f" % recall_score(y_test_c, base_pred))
print("기준 모델 네 칸짜리 표:\n", confusion_matrix(y_test_c, base_pred))