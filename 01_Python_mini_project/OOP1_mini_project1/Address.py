# Address Addr 클래스 아래의 요구사항을 반영하여 코드를 생성한다 - 이름, 전화번호, 이메일, 주소, 그룹

class Addr:
    def __init__(self, name, phone_number, email, address, group):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.group = group