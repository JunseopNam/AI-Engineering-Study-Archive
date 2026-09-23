# Gradient Descent

"""# 실습 1 - weieght 1번 업데이트하기
def udate_weight(w_t, learning_rate, gradient):
    w_next = w_t - (learning_rate * gradient)
    return w_next

# --- 테스트 코드 ---
current_w = 0.5
eta = 0.01 # 학습률
grad = 2.0 # 임의로 계산된 기울기

# 함수 호출
new_w = udate_weight(current_w, eta, grad)
print(f"업데이트된 가중치: {new_w}")
"""

# 실습 2 - 루프로 경사하강법 진행시켜서 2차 함수의 기울기가 0(또는 근접)하는 w 값 찾기
def gradient(w):
    return 2 * (w - 3)   # dE/dw

def gradient_descent(w_init, learning_rate, tolerance, max_iter):
    w = w_init
    history = [w]

    for t in range(max_iter):
        grad = gradient(w)                  # (2) 기울기
        w_next = w - learning_rate * grad   # (3) 이동
        history.append(w_next)

        if abs(w_next - w) < tolerance or grad == 0:
            return w_next, t + 1, history

        w = w_next

    return w, max_iter, history

# --- 테스트 코드 ---
current_w = 0
eta = 0.1 # 학습률
toler = 0.000001
max_iter = 100 

# 함수 호출
new_w = gradient_descent(current_w, eta, toler, max_iter)
print(f"업데이트된 가중치 history: {new_w}")