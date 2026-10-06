# ch08-3-1.py CNN 핵심 파이프라인(Feature Extraction & Flattening) 구현

"""
조건 1 (Zero-Padding): 연산 전, 가장자리에 정보 손실 및 특징 맵의 크기 축소 문제를 방지하기 위해 
입력 이미지 테두리에 0을 추가하는 Zero-Padding을 먼저 적용해야 합니다.

조건 2 (합성곱 연산): 커널이 이미지 위를 한 칸씩 이동(Sliding)하며 겹쳐진 영역의 요소들을 각각
곱하고 더하여 Output(특징 맵)의 값을 계산해야 합니다
"""

import numpy as np

def zero_padding(image):
    rows, cols = image.shape
    new_array = np.array([[0 for x in range(cols + 2)] for _ in range(rows + 2)])

    for r in range(rows):
        for c in range(cols):
            new_array[1 + r][1 + c] = image[r][c]

    return new_array

def conv2d(image, kernel):
    image_rows, image_cols = image.shape
    kernel_rows, kernel_cols = kernel.shape

    padded_image = zero_padding(image)
    new_array = np.array([[0 for x in range(image_cols)] for _ in range(image_rows)])

    for r in range(image_rows):
        for c in range(image_cols):
            window = padded_image[r : r + kernel_rows,
                                  c : c + kernel_cols]
            sum = 0
            for kr in range(kernel_rows):
                for kc in range(kernel_cols):
                    sum += window[kr, kc] * kernel[kr, kc]

            new_array[r,c] = sum
    return new_array


# 1. 테스트용 입력 이미지 생성 (5x5 크기)
test_image = np.array([
    [10, 10, 10, 0, 0],
    [10, 10, 10, 0, 0],
    [10, 10, 10, 0, 0],
    [ 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# 2. 3x3 커널 정의 (예: 라플라시안 외곽선 검출 필터)
test_kernel = np.array([
    [ 0, 1, 0],
    [ 1,-4, 1],
    [ 0, 1, 0]
])

# 3. 합성곱 연산 수행
result_feature_map = conv2d(test_image, test_kernel)

# 4. 결과 출력
print("=== 원본 입력 이미지 (5x5) ===")
print(test_image)

print("\n=== 적용된 커널 (3x3) ===")
print(test_kernel)

print("\n=== 합성곱 연산 결과 특징 맵 (5x5) ===")
print(result_feature_map)