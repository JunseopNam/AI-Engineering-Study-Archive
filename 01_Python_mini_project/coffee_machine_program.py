# coffee machine program 커피머신 프로그램

#dictionary
MENU = {
    "espresso" : {
        "ingrediants" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingrediants" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingrediants" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
    }
}

profit = 0.0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}


# definition
# 자원 충분 여부 확인
def is_resource_sufficient(order_ingrediants):
    if(resources.get("water") - MENU.get(order_ingrediants).get("ingrediants").get("water",0) < 0):
        print("죄송합니다. 물이 충분하지 않습니다")
        return False

    if(resources.get("milk") - MENU.get(order_ingrediants).get("ingrediants").get("milk", 0) < 0):
        print("죄송합니다. 우유가 충분하지 않습니다")
        return False

    if(resources.get("coffee") - MENU.get(order_ingrediants).get("ingrediants").get("coffee", 0) < 0):
        print("죄송합니다. 커피가 충분하지 않습니다")
        return False
    
    return True

# 동전 처리
def process_coins():
    quaters = input("동전을 넣어주세요 (쿼터 [$0.25]): ")
    dimes = input("동전을 넣어주세요 (다임 [$0.10]): ")
    nickels = input("동전을 넣어주세요 (니켈 [$0.05]): ")
    pennies = input("동전을 넣어주세요 (페니 [$0.01]): ")
    total_coin = float(quaters) * 0.25 + float(dimes) * 0.1 + float(nickels) * 0.05 + float(pennies) * 0.01
    print(f"투입한 금액: ${total_coin:.2f}")
    return total_coin

# 거래 성공 여부 확인
def is_transaction_successful(money_received, drink_cost):
    global profit
    if(money_received < drink_cost):
        print("죄송합니다. 금액이 $%.2f 부족합니다. 돈이 환불되었습니다." % (drink_cost - money_received))
        return False
    
    elif(money_received == drink_cost):
        profit += drink_cost

    else:
        print(f"${drink_cost}를 결제하고 남은 거스름돈 ${money_received - drink_cost:.2f}를 돌려드립니다")
        profit += drink_cost

    return True

# 커피 만들기
def make_coffee(drink_name, order_ingrediants):
    for item, amount in order_ingrediants.items():
        resources[item] -= amount

    print(f"여기 {drink_name}이(가) 나왔습니다. 즐기세요!")

# main
while(True):
    user = input("어떤 음료를 원하시나요? (espresso/latte/cappuccino): ")

    if(user == "off"):
        print("프로그램을 종료합니다.")
        exit()

    elif(user == "report"):
        for i, (name, amount) in enumerate(resources.items(), start=1):
            print(f"{i}. {name}: {amount}")
        print("돈: $%.2f"%profit)

    elif(user == "1" or user == "espresso" or user == "에스프레소"):
        if (is_resource_sufficient("espresso")):
            money = process_coins()
            if(is_transaction_successful(money, MENU.get("espresso").get("cost"))):
                make_coffee("espresso",  MENU.get("espresso").get("ingrediants"))

    elif(user == "2" or  user == "latte" or  user == "라떼"):
         if (is_resource_sufficient("latte")):
            money = process_coins()
            if(is_transaction_successful(money, MENU.get("latte").get("cost"))):
                make_coffee("latte",  MENU.get("latte").get("ingrediants"))

    elif(user == "3" or  user == "cappuccino" or  user == "카푸치노"):
        if (is_resource_sufficient("cappuccino")):
            money = process_coins()
            if(is_transaction_successful(money, MENU.get("cappuccino").get("cost"))):
                make_coffee("cappuccino",  MENU.get("cappuccino").get("ingrediants"))

    else:
        print("잘못된 값입니다. 다시 입력해주세요")