# unsupervised_learning 1.clustring

import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# 1단계 - 데이터 불러오기
data = load_iris()
X = data.data            # 꽃 150송이 x 네 가지 길이

# 2단계 - 모델 만들기
km = KMeans(n_clusters=3, random_state=42, n_init=10)  # TODO: 3무리

# 3단계 - 무리 만들기
km.fit(X)               # TODO: 무엇을 넣어야 할까요?

# 4단계 - 결과 살펴보기
labels = km.labels_          # TODO: 각 꽃의 무리 번호를 꺼내세요
print("무리별 인원 =", np.bincount(labels))
print("무리 안 흝어진 정도 = %.2f" % km.inertia_)    # TODO
print("무리 중심점:")
print(np.round(km.cluster_centers_ , 2))    # TODO: 중심점을 꺼내세요

# 5단계 - 실제 품종과 비교해 보기
for c in range(3):
    m = labels == c
    print("무리", c, "인원", m.sum(), np.bincount(data.target[m], minlength=3))