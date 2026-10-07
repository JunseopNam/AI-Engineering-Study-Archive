# ch6-1-2.py YOLO 클래스별 신뢰도와 최종 판정
"""
조건
NumPy 브로드캐스팅으로 3x3 점수 행렬을 한 번에 계산
np.argmax로 예측 박스별 최댓값 클래스 선택
임계값(THRESHOLD) = 0.5
출력 형식: '박스 0: 자동차 (0.72)' 또는 '박스 1: 제거'
"""
import numpy as np
THRESHOLD = 0.5

classification = ["자동차", "자전거", "보행자"]

predict_box = np.array([
    [0.80, 0.15, 0.05],
    [0.10, 0.20, 0.70],
    [0.20, 0.70, 0.10]
])

confidence = np.array([
    [0.9],
    [0.3],
    [0.8]   
])

pr = predict_box * confidence   # array길이가 달라도 numpy가 브로드캐스팅해줌
box_max = np.argmax(pr, axis=1)   # np.argmax 써서 박스별 최댓값 선택

for i in range(len(box_max)):
    cls_idx = box_max[i]
    max_score = pr[i, cls_idx]

    if  max_score >= THRESHOLD:
        print(f"박스 {i}: {classification[cls_idx]} ({max_score:.2f})")
    else:
        print(f"박스 {i}: 제거")