# game 숫자 맞히기 게임

divider1 = "=" * 34
divider2 = "-" * 34

answer = 37
count = 0
history = []

while(count < 5):
    count = count + 1
    guess = int(input(f"[{count}/5] 숫자를 입력하세요 (1~100):"))
    history.append(guess)

    if(answer == guess):
        print(f"정답입니다! {count}번 만에 맞혔습니다.")
        break

    elif(answer < guess):
        print("DOWN! 더 작은 수를 입력하세요.")

    elif(answer > guess):
        print("UP! 더 큰 수를 입력하세요.")

result = "성공" if guess == answer else "실패"
too_big = [g for g in history if g > answer]
too_small = [g for g in history if g < answer]

print(divider1)
print(f"{'게임결과':^17}")
print(divider1)
print(f"{'정답':<14}{answer:>18}")
print(f"{'시도 횟수':<14}{count:>18}")
print(f"{'결과':<14}{result:>18}")
print(divider2)
print(f"{'입력기록':<14}{str(history):>18}")
print(f"{'너무 큰 수':<14}{len(too_big):>18}")
print(f"{'너무 작은 수':<14}{len(too_small):>18}")
print(divider1)