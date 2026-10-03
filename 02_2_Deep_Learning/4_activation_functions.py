# ch07-8-1.py 활성화 함수와 도함수 구현하기

import numpy as np
from math import e

"""
문제: NumPy를 사용하여 sigmoid 함수와 relu 함수, 그리고 오차역전파 시 기울기 계산에 필요한 각각의 도함수(derivative)를 구현하기
조건:
1. sigmoid(x)와 sigmoid_derivative(x) 함수를 구현할 것.
2. relu(x) 함수는 입력값 x가 0보다 크면 x를, 그렇지 않으면 0을 반환하도록 구현할 것
3. relu_derivative(x) 함수는 입력값 x가 0보다 크면 1을, 그렇지 않으면 0을 반환하도록 구현할 것
"""

# sigmoid
def sigmoid(x):
    x = np.array(x)
    array_x = np.zeros_like(x, dtype=float)

    for i in range(len(x)):
        array_x[i] = 1 / (1 + e**(-x[i]))

    return array_x

def sigmoid_integer(x):
    return 1 / (1 + e**(-x))

def sigmoid_derivative(x):
    x = np.array(x)
    array_x = np.zeros_like(x, dtype=float)

    for i in range(len(x)):
        array_x[i] = sigmoid_integer(x[i]) * (1 - sigmoid_integer(x[i]))

    return array_x


# relu
def relu(x):
    x = np.array(x)
    array_x = np.zeros_like(x, dtype=float)

    for i in range(len(x)):
        if x[i] > 0:
            array_x[i] = x[i]
        else:
            array_x[i] = 0
            
    return array_x

def relu_derivative(x):
    x = np.array(x)
    array_x = np.zeros_like(x, dtype=float)
    
    for i in range(len(x)):
        if x[i] > 0:
            array_x[i] = 1
        else:
            array_x[i] = 0
            
    return array_x


test_x = np.array([-2, -0.5, 0, 0.5, 2 ])
print('입력값 x:')
print(test_x)
print('----------------------------------------------')
print('1. sigmoid 함수 테스트 결과')
print('sigmoid(x):')
print(sigmoid(test_x))
print('sigmoid_derivative(x):')
print(sigmoid_derivative(test_x))
print('----------------------------------------------')
print('2. ReLu 함수 테스트 결과')
print('relu(x):')
print(relu(test_x))
print('relu_derivative(x):')
print(relu_derivative(test_x))
