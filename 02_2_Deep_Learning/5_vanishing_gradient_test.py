# ch07-8-2 기울기 소실 시뮬레이션 테스트

# 공통 설정: 10개의 은닉층, 초기 기울기 1.0
hidden_size = 10
base_gradient = 1.0
print(f"설정: 은닉층 수 = {hidden_size}, 초기 기울기 = {base_gradient}")

# 1. 시그모이드 네트워크 (매 층마다 시그모이드 도함수의 최댓값 0.25 곱하기)
grad_sigmoid = base_gradient
for _ in range(hidden_size):
    grad_sigmoid *= 0.25
print(f"Sigmoid 네트워크 10층 통과 후 최종 기울기: {grad_sigmoid:.10f}")
print("결과 분석: 기울기가 0에 가깝게 매우 작아져 기울기 소실(Gradient Vanishing)이 발생함을 확인할 수 있다.")

# 2. ReLU 네트워크 (매 층마다 양수니까 1 곱하기)
grad_relu = base_gradient
for _ in range(hidden_size):
    grad_relu *= 1.0
print(f"ReLU 네트워크 10층 통과 후 최종 기울기: {grad_relu}")
print("기울기가 1.0으로 유지되어 깊은 층에서도 기울기 소실 없이 학습이 가능함을 확인할 수 있다.")
