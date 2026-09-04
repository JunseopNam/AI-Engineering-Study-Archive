# playist 음악 재생목록 관리 프로그램

from collections import deque

queue = deque() # 재생 대기열 - 큐(FIFO)
history = []    # 재생 이력 - 스택(LIFO)
now = None      # 현재 재생중인 곡


# function
# 현재 상태 출력 함수
def show_status(now):
    divider1 = "=" * 44
    divider2 = "-" * 44

    if now == None or now == "":
        now = "(없음)"

    print(divider1)
    print(f"{'M Y  P L A Y I S T':^44}")
    print(divider1)
    print(f"{'현재 재생':<5} {now:>15}")
    print(divider2)
    print(f"{'대기열':<5} {len(queue):>5}곡 (먼저 넣은 곡부터 재생)")

    if len(queue) == 0:
        print(" (비어 있음)")
    else:
        for i, s in enumerate(queue, 1):
            print(f" {i}. {s}")

    print(divider2)
    print(f"{'재생 이력':<5} {len(history):>5}곡 (최근에 들은 곡부터)")

    if len(queue) == 0:
        print(" (비어 있음)")
    else:
        for i, s in enumerate(reversed(history), 1):
            print(f" {i}. {s}")
            
    print(divider1)


# 곡 추가 함수
def add_song(title):
    queue.append(title)
    print(f"{title}을(를) 대기열 맨 뒤에 추가했습니다. (총 {len(queue)}곡)\n")


# 다음 곡 재생
def play_next(now):
    if now is not None:
        if queue == None or queue == "":
            print("대기열이 비었습니다.")
            return now
        history.append(now)
        now = queue.popleft()
        print(f"재생: {now}")
        return now
    else:
        print("재생 중인 곡이 없습니다.")


# 이전 곡으로
def play_prev(now):
    if len(history) != 0:
        queue.appendleft(now)
        print("이전 곡 재생: %s" % (now))
        now = history.pop()
        return now
    else:
        print("재생 이력이 비어있습니다")
        return now


# 급한 곡 끼워 넣기
def add_urgent(title):
    queue.appendleft(title)
    print(f"'{title}'을(를) 대기열 맨 앞에 넣었습니다. (총{len(queue)}곡)")


# 대기열 순서 회전
def rotate_queue(n):
    if len(queue) == 0:
        print("대기열이 비었습니다.")
        return

    queue.rotate(n)
    print("대기열을 %d칸 회전했습니다" % (n))
    print(list(queue))


# main
MENU = """
1.곡 추가     2.다음 곡     3.이전 곡
4.맨 앞에 넣기   5.대기열 회전   6.현재 상태   0.종료"""
now = None
print(MENU)

while(True):
    print()
    menu = input("번호를 선택하세요: ")

    if menu == "1" or menu == "곡 추가" or menu == "곡추가":
        now = input("추가할 곡 제목: ")
        add_song(now)

    elif menu == "2" or menu == "이전 곡" or menu == "이전곡":
        now = play_prev(now)

    elif menu == "3" or menu == "다음 곡" or menu == "다음곡":
        now = play_next(now)

    elif menu == "4" or menu == "맨 앞에 넣기" or menu == "맨앞에넣기" or menu == "맨 앞에넣기" or menu == "맨앞에 넣기":
        title = input("다음에 재생할 곡: ")
        add_urgent(title)
      
    elif menu == "5" or menu == "대기열 회전" or menu == "대기열회전":
            turn = int(input("우측으로 회전시킬 칸 수: "))
            rotate_queue(turn)
    
    elif menu == "6" or menu == "현재 상태" or menu == "현재상태":
        show_status(now)
    
    elif menu == "0" or menu == "종료":
        print("프로그램을 종료합니다.")
        exit()

    else:
        print("없는 번호입니다.")