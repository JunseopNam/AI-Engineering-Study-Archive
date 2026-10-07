# ch6-1 k-NN 기반 차량 분류
import numpy as np

def euclidean_distance(array1, array2):
    if len(array1) == len(array2):
        sum = 0
        for i in range(len(array1)):
            sum += (array1[i] - array2[i]) ** 2
        distance = sum ** (1/2)
    else:
        print("차원이 다릅니다.")
        return None
    
    return distance

def k_nn_1(object, **candidates):
    distance = float('inf')
    best_name = None
    for name, data in candidates.items():
        if distance > euclidean_distance(object, data):
            distance = euclidean_distance(object, data)
            best_name = name

    print(f"분류 결과 가장 가까운 차량: {best_name} (거리: {distance:.4f})")
    return best_name


# 확장 과제
from collections import Counter
import numpy as np

def euclidean_distance(array1, array2):
    if len(array1) == len(array2):
        diff_sq_sum = 0
        for i in range(len(array1)):
            diff_sq_sum += (array1[i] - array2[i]) ** 2
        return diff_sq_sum ** (1/2)
    else:
        print("차원이 다릅니다.")
        return None

def k_nn_3(target, **candidates):
    names = []
    distances = []

    for name, data in candidates.items():
        dist = euclidean_distance(target, data)
        names.append(name)
        distances.append(dist)

    sorted_indices = np.argsort(distances)
    nearest_indices = sorted_indices[:3]

    top_k_names = [names[i] for i in nearest_indices]
    print(f"가장 가까운 3대: {top_k_names}")

    vote_name = [name.split('_')[0] for name in top_k_names]
    vote_counter = Counter(vote_name)
    majority_name, count = vote_counter.most_common(1)[0]

    print(f"최종 판정 차량: {majority_name} ({count}표 획득)")
    return majority_name


new_car = np.array([0.55, 0.45, 0.62, 0.48])

car_db = {
    "suv_1": np.array([0.52, 0.48, 0.60, 0.51]),
    "suv_2": np.array([0.54, 0.46, 0.61, 0.49]),
    "bus_1": np.array([0.80, 0.70, 0.60, 0.40]),
    "bus_2": np.array([0.78, 0.72, 0.62, 0.38]),
    "truck_1": np.array([0.70, 0.60, 0.80, 0.20]),
    "suv_3": np.array([0.50, 0.50, 0.60, 0.50])
}

dataset = {
    "suv": np.array([0.52, 0.48, 0.60, 0.51]),
    "suv_b": np.array([0.54, 0.46, 0.61, 0.49]),
    "bus": np.array([0.80, 0.70, 0.60, 0.40]),
    "truck": np.array([0.70, 0.60, 0.80, 0.20])
}

k_nn_1(new_car, **car_db)

k_nn_3(new_car, **car_db)