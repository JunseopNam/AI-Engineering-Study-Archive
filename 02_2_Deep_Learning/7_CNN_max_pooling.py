# ch08-3-2-3.py 문제 2. 임계값 처리 (Thresholding) - ReLU 활성화 함수 적용
#               문제 3. 특징 압축 - 풀링(Pooling) 연산 구현

"""
조건: ReLU(Rectified Linear Unit) 함수를 적용하여, 특징 맵의 음수 값은 0으로 무시하고 양수는
그대로 통과시키도록 처리하세요. 이를 통해 네트워크에 비선형성(Non-linearity)을 부여합니다

조건: 2x2 크기의 윈도우를 사용하는 Max Pooling 함수를 구현하세요. 해당 영역에서 가장 뚜렷한
특징(가장 큰 값)만 살아남아 강조되도록 1개의 픽셀로 압축해야 합니다. (참고: 가중치 연산 없이 고정된
연산만 수행합니다.)
"""

import numpy as np


# ch08-3-2-3.py
def apply_relu(feature_map):
    rows, cols = feature_map.shape
    new_array = feature_map.copy()
    for r in range(rows):
        for c in range(cols):
            if new_array[r][c] <= 0:
                new_array[r][c] = 0

    return new_array

def max_pooling_2x2(relu):
    relu_rows, relu_cols = relu.shape
    window_size = 2

    out_rows = relu_rows // window_size
    out_cols = relu_cols // window_size
    new_array = np.array([[0 for _ in range(out_cols)] for _ in range(out_rows)])
    for r in range(out_rows):
            for c in range(out_cols):
                window = relu[r * window_size : r * window_size + window_size, c * window_size : c * window_size + window_size]
                max_value = window[0][0]

                for wr in range(window_size):
                    for wc in range(window_size):
                        if window[wr][wc] > max_value:
                            max_value = window[wr][wc]
                new_array[r][c] = max_value        
    return new_array


# 1. 테스트용 입력 특징 맵 생성 (4x4크기, 음수 값 포함)
test_feature_map = np.array([
    [ 1.5,-0.5, 2.0,-1.0],
    [-2.0, 3.0, 0.5, 1.0],
    [ 0.0,-1.5, 4.0, 2.5],
    [ 1.0, 2.0,-3.0,-2.5]
])

# 2.문제 2: ReLU 활성화 함수 적용
relu_result = apply_relu(test_feature_map)

# 3.문제 3: Max Pooling 적용 (ReLU 통과 결과를 입력으로 사용)
pooling_result = max_pooling_2x2(relu_result)

# 4.결과 출력
print("=== 1. 원본 특징 맵 (4x4) ===")
print(test_feature_map)

print("\n=== 2. ReLU 활성화 함수 적용 결과 (4x4) ===")
print(relu_result)

print("\n=== 3. MAx Pooling (2x2) 적용 결과 (2x2) ===")
print("설명: 2x2 영역마다 가장 큰 값을 추출하여 크기가 4x4에서 2x2로 압축되었습니다.")
print(pooling_result)
