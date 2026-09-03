# money 용돈 기록장

import sys

FILE = "9_03/records.txt"
CATEGORIES = ["식비", "교통", "문화", "기타"]

# function
# 파일에 한 줄 덧붙여 쓴다 ('a'모드)
def add_records(date, category, item, amount):
    with open(FILE, 'a', encoding="utf-8") as f:
        f.write(f"{date},{category},{item},{amount}\n")
    print(f"기록 했습니다. ({date} {category} {item} {int(amount):,}원)")


# 파일을 읽어 리스트로 만들기
def load_records():
    with open(FILE, 'a', encoding="utf-8") as f:
        pass

    records = []
    with open(FILE, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: continue

            date, category, item, amount = line.split(',')
            record = {'date': date, 'category': category, 'item': item, 'amount': int(amount)}
            records.append(record)
    return records


# 전체 목록을 표로 출력하기
def show_all():
    divider1 = "=" * 46
    divider2 = "-" * 46
    records = load_records()

    if len(records) == 0:
        print("아직 기록이 없습니다.")
    else:   
        print(divider1)
        print(f"{'용 돈 기 록 장':^23}")
        print(divider1)
        print(f"{'번호':<5}{'날짜':<8}{'분류':<5}{'내용':<13}{'금액':<9}")
        print(divider2)
        for i, r in enumerate(records, 1):
            print(f"{i:<5}{r['date']:<12}{r['category']:<5}{r['item']:<13}{r['amount']:<9,}")
        print(divider2)
        print(f"{'합계':<5}{sum([r['amount'] for r in records]):>25,}")
        print(divider1)

# 분류별 통계 내기
def summary():
    records = load_records()

    if not records:
        print("아직 기록이 없습니다.")
        return

    by_category = {}
    total_amount = 0

    for c in records:
        categories = c['category']
        total_amount += int(c['amount'])

        if categories in by_category:
            by_category[categories] += int(c['amount'])
        else:
            by_category[categories] = int(c['amount'])

    sorted_categories = sorted(by_category, key=lambda k:by_category[k], reverse=True)

    divider = "-" * 46
    print(divider)
    print(f"{'분류별 지출':^38}")
    print(divider)

    for c in sorted_categories:
        cost = by_category[c]
        ratio = (cost / total_amount) * 100
        print(f"{c:<8}{cost:>10,}원{ratio:>8.1f}%")

    count = len(records)
    avgerage = int(total_amount / count)

    print(divider)
    print(f"{'총 지출':<8}{total_amount:>10,}원")
    print(f"{'기록 수':<8}{count:>10}건")
    print(f"{'평균':<8}{avgerage:>10,}원")
    print(divider)


# 검색하기
def search(word):
    records = load_records()
    found = [r for r in records if word in r["item"] or word in r["category"]]
    print(f"'{word}' 검색 결과: {len(found)}건")

    total = 0
    for i, r in enumerate(found, 1):
        amount = int(r["amount"])
        total += amount
        print(f"{i}. {r['date']} {r['category']} {r['item']} {amount:,}원")

    if len(found) > 0:
        print(f"합계 {total:,}원")


# 메뉴 루프로 조립하기
def menu_loop():
    while True:
        print("1. 기록 추가  2. 전체 보기  3. 통계\n4. 검색  0. 종료")
        choice = input("번호를 선택하세요: ")

        if choice == "1":
            date = input("날짜(예: 2026-08-24): ")
            print(f"분류: {CATEGORIES}")
            category = input("분류: ")

            if category not in CATEGORIES:
                print("없는 분류입니다. 메뉴로 돌아갑니다.\n")
                continue

            item = input("내용: ")
            amount = int(input("금액: "))

            add_records(date, category, item, amount)

        elif choice == "2":
            show_all()

        elif choice == "3":
            summary()

        elif choice == "4":
            word = input("검색어: ")
            search(word)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("없는 번호입니다.")



# main
args = sys.argv[1:]

if len(args) > 0:
    cmd = args[0]

    if cmd == "list":
        show_all()

    elif cmd == "sum":
        summary()

    elif cmd == "find" and len(args) > 1:
        search(args[1])
        
    else:
        print("사용법: python money.py [list | sum | find 검색어]")

else:
    menu_loop()