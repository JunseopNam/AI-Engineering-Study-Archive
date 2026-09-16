# student_perceptron

import numpy as np

# 데이터 국어 수학 영어 과학
X = np.array([[70,100,70,80], [90,60,80,80], [90,90,90,100], [85,70,95,75],
              [100,55,85,90], [60,95,65,70], [85,85,75,85], [70,90,70,75],
              [95,65,85,75], [80,75,70,70], [90,85,90,95], [85,70,75,70]], float)
y = np.array([1,0,1,0, 0,1,1,1, 0,0,1,0])    # 1=합격, 0=불합격

# 1단계 - 초기설정
w = np.array([0.1, 0.2, 0.3, 0.1])
b = -20.0
eta = 0.005

for epoch in range(11):
    # 정확도 먼저 기록
    pred_all = (X @ w + b >= 0).astype(int)
    acc = (pred_all == y).sum()                # TODO
    print("에포키 %2d 정확도 %2d/12" % (epoch, acc))

    for i in range(len(X)):
        net = X[i] @ w + b             # TODO: 곱해서 더하기
        pred = 1 if net >= 0 else 0    # TODO: 계단함수
        err = y[i] - pred              # TODO: 오차
        w = w + eta * err * X[i]       # TODO
        b = b + eta * err
