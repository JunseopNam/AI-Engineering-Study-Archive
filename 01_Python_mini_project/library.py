# library 도서관 대출 관리 시스템

from abc import ABC, abstractmethod

# Library Item Class
class LibraryItem(ABC):
    total_items = 0

    def __init__(self, title, item_id):
        self.is_loaned = False
        self.borrower = None
        self.title = title
        self.item_id = item_id
        LibraryItem.total_items += 1

    @abstractmethod
    def loan_period():
        pass

    @abstractmethod
    def info():
        pass

    def checkout(self, name):
        if self.is_loaned == True:
            print(f"'{self.title}'은(는) 이미 {self.borrower}님이 대출 중입니다.")
            return False

        self.is_loaned = True
        self.borrower = name
        print(f"{name}님, '{self.title}' 대출 완료! (대출 기간 {self.loan_period()}일)")
        return True

    def return_item(self):
        if self.is_loaned == False:
            print("반납할 아이템이 없습니다")
            return False

        print(f"{self.borrower}님이 '{self.title}'을(를) 반납했습니다.")
        self.is_loaned = False
        self.borrower = None
        return True


# Book Class
class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages      

    def loan_period(self):
        return 14

    def info(self):
        return f"[도서] {self.title} / {self.author} / {self.pages}"  


# DVD Class
class DVD(LibraryItem):
    def __init__(self, title, item_id, director, minutes):
        super().__init__(title, item_id)
        self.director = director
        self.minutes = minutes

    def loan_period(self):
        return 7

    def info(self):
        return f"[DVD] {self.title} / {self.director} 감독 / {self.minutes}분"  

# Magazine Class
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def loan_period(self):
        return 3

    def info(self):
        return f"[잡지] {self.title} / {self.issue}호"  


# Library Class
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"'{item.title}' 등록 완료 (총 {len(self.items)}개)")

    def find(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def show_all(self):
        divider1 = "=" * 56
        divider2 = "-" * 56

        print(divider1)
        print(f"{self.library_name:^50}")
        print(divider1)
        print(f"{'ID':<6} {'정보':<32} {'상태':>14}")
        print(divider2)
        for item in self.items:
            state = f"대출중({item.borrower})" if item.is_loaned else "대출가능"
            print(f"{item.item_id:<6} {item.info():<32} {state:>14}")
        print(divider1)

    def report(self):
        divider = "-" * 56
        items_count = {}
        for item in self.items:
            if type(item).__name__ not in items_count:
                items_count[type(item).__name__] = 1
            else:
                items_count[type(item).__name__] += 1

        print(divider)
        print(f"{'종류별 등록 현황':^40}")
        print(divider)
        for kind in sorted(items_count, key=lambda x: items_count[x], reverse=True):
            print(f"{kind:<6} {items_count[kind]:>25}개")
        print(divider)
        print(f"{'대출 중':<15} {len([i for i in self.items if i.is_loaned]):>15}개")
        print(f"{'전체 등록':<15} {LibraryItem.total_items:>15}개")
        print(divider)


# mian
lib = Library("한 빛 도 서 관")

lib.add(Book("클린 코드", "B002", "로버트 마틴", 464))
lib.add(Book("해리 포터와 마법사의 돌", "B003", "J.K. 롤링", 320))
lib.add(Book("어린 왕자", "B004", "생텍쥐페리", 136))
lib.add(Book("자료구조와 알고리즘", "B005", "나동빈", 600))
lib.add(Book("1984", "B006", "조지 오웰", 350))

lib.add(Magazine("내셔널지오그래픽", "M002", 10))
lib.add(Magazine("씨네21", "M003", 11))
lib.add(Magazine("월간 디자인", "M004", 8))
lib.add(Magazine("포브스 코리아", "M005", 12))

lib.add(DVD("인셉션", "D002", "크리스토퍼 놀란", 148))
lib.add(DVD("기생충", "D003", "봉준호", 132))
lib.add(DVD("센과 치히로의 행방불명", "D004", "미야자키 하야오", 125))
lib.add(DVD("라라랜드", "D005", "데이미언 셔젤", 128))
lib.add(DVD("어벤져스: 엔드게임", "D006", "루소 형제", 181))

while(True):
    print("1.전체 목록  2.통계  3.대출 4.반납  0.종료")
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        lib.show_all()

    elif choice == "2":
        lib.report()

    elif choice == "3":
        item_number = input("대출할 자료 번호: ").upper()
        if lib.find(item_number) == None:
            print("없는 자료 번호 입니다.")
            continue
        borrower_name = input("대출자 이름: ")
        item = lib.find(item_number)
        item.checkout(borrower_name)

    elif choice == "4": #return_item
        item_number = input("반납할 자료 번호: ").upper()
        if lib.find(item_number) == None:
                print("없는 자료 번호 입니다.")
                continue
        item = lib.find(item_number)
        item.return_item()
        

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
        
    else:
        print("없는 번호입니다.")