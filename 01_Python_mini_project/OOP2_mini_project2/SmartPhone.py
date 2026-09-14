# SmartPhone - 연락처 정보 관리 -> Addr 클래스의 인스턴스 10개를 저장할 수 있는 리스트 정의, 리스트에 인스턴스를 저장, 수정, 삭제, 저장된 리스트 출력 메소드 정의
from Address import Addr, CompanyAddr, CustomerAddr

class SmartPhone:
    def __init__(self):
        self.address_list = []

    # 키보드로 부터 입력 받아 객체를 생성함
    def inputAddrData(self, type_number):
        name = input("이름을 입력하세요: ")
        phone_number = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        birthday = input("생일을 입력하세요 (예 1990-01-01): ")
        rank = input("직급을 입력하세요: ")

        if type_number == '1':
            company_name = input("회사 이름을 입력하세요: ")
            department = input("부서를 입력하세요: ")
            addr = CompanyAddr(name, phone_number, email, address, birthday, company_name, department, rank)

        elif type_number == '2':
            customer_name = input("회사 이름을 입력하세요: ")
            item_name = input("부서를 입력하세요: ")
            addr = CustomerAddr(name, phone_number, email, address, birthday, customer_name, item_name, rank)

        elif type_number == '0':
            group = input("그룹(친구/가족)을 입력하세요: ")
            addr = Addr(name, phone_number, email, address, group)

        self.addAddr(addr)
        print(f">>>> 데이터가 저장되었습니다.(현재 {len(self.address_list)}개)\n")

    # 연락처에 객체 저장
    def addAddr(self, address):
        self.address_list.append(address)

    # 객체 정보 출력
    def printAddr(self, address):
        if address in self.address_list :
            address.printInformation()
        else:
            print("해당 연락처를 찾을 수 없습니다.")
            

    # 모든 연락처 출력
    def printAllAddr(self):
        for index, addr in enumerate(self.address_list, 1):
            print(f"[{index}]")
            self.printAddr(addr)
            print("")

    # 연락처 검색
    def searchAddr(self, name : str):
        search_list = [l for l in self.address_list if l.name == name]
        length = len(search_list)
        if length == 0:
            return None
        
        elif length == 1:
            return search_list[0]
        
        else:
            print("같은 이름이 여러명 발견되었습니다.")
            for num, address in enumerate(search_list, 1):
                print(f"[{num}]")
                self.printAddr(address)

            while True:
                number = int(input("선택할 번호를 입력해 주세요 (0 입력시 취소): "))
                if 0 < number and number <= length:
                    return search_list[number - 1]
                elif number == 0:
                    print("검색이 취소 되었습니다")
                    return None
                else:
                    print("다시 입력해주세요")
                    continue

    # 연락처 삭제
    def deleteAddr(self, name : str):
        address = self.searchAddr(name)
        if address != None :
            print("연락처가 삭제 되었습니다.")
            self.address_list.remove(address)
        else:
            print("존재하지 않는 연락처 입니다.")

    # 연락처 수정
    def editAddr(self, name : str):
        addr = self.searchAddr(name)
        if addr != None :
            string = " 7.부서(품목)명 8.직급" if type(addr) == CompanyAddr or type(addr) == CustomerAddr else " "
            number = int(input(f"수정하고 싶은 부분을 선택하세요\n1.이름 2.전화번호 3.이메일 4.주소 5.그룹(회사,거래처)명 6.생일{string}: "))
            if number == 1:
                new_name = input("이름을 변경해 주세요: ")
                addr.name = new_name

            elif number == 2:
                new_phone_number = input("전화번호를 변경해 주세요: ")
                addr.phone_number = new_phone_number

            elif number == 3:
                new_email = input("이메일을 변경해 주세요: ")
                addr.email = new_email

            elif number == 4:
                new_addr = input("주소을 변경해 주세요: ")
                addr.address = new_addr
            
            elif number == 5:
                if type(addr) == CompanyAddr:
                    new_group = input("회사명을 변경해 주세요: ")
                    addr.group = new_str

                elif type(addr) == CustomerAddr:
                    new_group = input("거래처명을 변경해 주세요: ")
                    addr.group = new_str

                elif type(addr) == Addr:
                    new_group = input("그룹을 변경해 주세요: ")
                    addr.group = new_group

            elif number == 6:
                new_birthday = input("생일을 변경해 주세요: ")
                addr.birthday = new_birthday

            elif number == 7:
                if type(addr) == CompanyAddr:
                    new_str = input("부서을 변경해 주세요: ")
                    addr.department_name = new_str

                elif type(addr) == CustomerAddr:
                    new_str = input("품목을 변경해 주세요: ")
                    addr.item_name = new_str

                else:
                    print("잘못된 입력입니다. 돌아갑니다")

            elif number == 8:
                if type(addr) == CompanyAddr or type(addr) == CustomerAddr:
                    new_rank = input("직급을 변경해 주세요: ")
                    addr.rank = new_rank
                else:
                    print("잘못된 입력입니다. 돌아갑니다")

            else:
                print("잘못된 입력입니다. 돌아갑니다")

        else:
            print("존재하지 않는 연락처 입니다.")
