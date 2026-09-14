# Address Addr 기본정보를 저장하고, 기본 정보를 출력하는 메소드를 정의합니다 - 이름, 전화번호, 이메일, 주소, 그룹, 생일

class Addr:
    def __init__(self, name, phone_number, email, address, group, birthday):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.group = group
        self.birthday = birthday

    def printInformation(self):
        print(f"이름: {self.name}")
        print(f"전화번호: {self.phone_number}")
        print(f"이메일: {self.email}")
        print(f"그룹(회사/거래처): {self.group}")
        print(f"생일: {self.birthday}")


# CompanyAddr class
class CompanyAddr(Addr):
    def __init__(self, name, phone_number, email, address, birthday, company_name, department_name, rank):
        super().__init__(name, phone_number, email, address, company_name, birthday)
        self.department_name = department_name
        self.rank = rank

    def printInformation(self):
        super().printInformation()
        print(f"직급: {self.rank}")
        print(f"부서: {self.department_name}")


# CustomerAddr class
class CustomerAddr(Addr):
    def __init__(self, name, phone_number, email, address, birthday, customer_name, item_name, rank):
        super().__init__(name, phone_number, email, address, customer_name, birthday)
        self.item_name = item_name
        self.rank = rank

    def printInformation(self):
        super().printInformation()
        print(f"직급: {self.rank}")
        print(f"품목: {self.item_name}")
