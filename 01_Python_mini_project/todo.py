# todo 할 일 관리 프로그램

divider1 = "=" * 30
divider2 = "-" * 30

todos = []
prompt = """1. 할 일 추가
2. 할 일 삭제
3. 목록 보기
4. 검색하기
5. 종료
"""

while(True):
    print(prompt)
    work = int(input("번호를 선택하세요:"))

    if(work == 5):
        print("프로그램을 종료합니다.")
        break

    elif(work == 1):
        todos.append(input("추가할 할 일: "))
        for count, todo in enumerate(todos, 1):
            print(f"'{todo}' 추가했습니다. (현재{count}개)") 

    elif(work == 2):
        if(len(todos) != 0):
            for count, todo in enumerate(todos, 1):
                print(f"{count}. {todo}") 
            
            num = int(input("삭제할 번호: "))

            if(1 <= num <= len(todos)):
                print(f"'{todos.pop(num - 1)}'가 삭제했습니다. (남은 {len(todos)}개)")

            else :
                print("없는 번호입니다.")
                
        else:
            print("삭제할 할 일이 없습니다.")

    elif(work == 3):
        print(divider1)
        print(f"{'할 일 목록':^15}")
        print(divider1)

        if(len(todos) != 0):
            for count, todo in enumerate(todos, 1):
                print(f"{count:>2}. {todo}") 

        else:
            print("등록된 할 일이 없습니다.")

        print(divider2)
        print(f"총 {len(todos)}개")
        print(divider1)
    
    elif(work == 4):
        word = input("검색할 단어: ")
        found = [t for t in todos if word in t]

        print(f"'{word}' 검색 결과 {len(found)}개")
        for count, find in enumerate(found, 1):
            print(f"{count:>2}. {find}") 
    
    else:
        print("1~5 중에서 골라주세요.")
    
                