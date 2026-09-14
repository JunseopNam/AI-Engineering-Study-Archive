# SmartPhoneMain
from SmartPhone import SmartPhone, Addr

class SmartPhoneMain:
    def printMenue(self):
        Menu = '''Contact Manager
-------------------
1. 연락처 등록 (회사)
2. 연락처 등록 (거래처)
3. 모든 연락처 출력
4. 연락처 검색
5. 연락처 삭제
6. 연락처 수정
7. 프로그램 종료
-------------------
'''
        print(Menu)

    def Start(self):
        self.s = SmartPhone()
        addr1 = Addr("홍길동", "010-1234-5678", "honghong@naver.com", "서울 종로3가", "친구", "2000-01-01")
        addr2 = Addr("이영희", "010-5555-1234", "yh_lee@gmail.com", "대구 수성구", "가족", "1975-12-12")
        self.s.addAddr(addr1)
        self.s.addAddr(addr2)

        while(True):
            self.printMenue()
            choice = input("원하시는 작업을 선택하세요 (1-7): ")
            print("")

            if choice == '1':
                print("# 연락처 등록(회사)")
                self.s.inputAddrData(choice)

            elif choice == '2':
                print("# 연락처 등록(거래처)")
                self.s.inputAddrData(choice)

            elif choice == '3':
                self.s.printAllAddr()

            elif choice == '4':
                name = input("찾으시는 연락처의 이름을 검색하세요:")
                address = self.s.searchAddr(name)
                if address != None:
                    print(f"'{name}' 검색결과 입니다")
                    self.s.printAddr(address)
                else:
                    print("검색 결과가 없습니다. 메뉴로 돌아갑니다.")

            elif choice == '5':
                name = input("지우려는 연락처의 이름을 검색하세요:")
                self.s.deleteAddr(name)

            elif choice == '6':
                name = input("수정하는 연락처의 이름을 검색하세요:")
                self.s.editAddr(name)
        
            elif choice == '7':
                print("프로그램을 종료합니다.")
                break
        
            else:
                print("없는 번호입니다.")

if __name__ == "__main__":
    s = SmartPhoneMain()
    s.Start()
