# stack 구현하기

"""
Stack 인터페이스(interface)와 StackNode
"""

from abc import ABC, abstractmethod

class Stack(ABC):
    """Java의 interface Stack에 대응하는 추상 클래스(abstract class)"""

    @abstractmethod
    def is_empty(self) -> bool:...

    @abstractmethod
    def push(self, data) -> None:...

    @abstractmethod
    def pop(self) -> str:...

    @abstractmethod
    def delete(self, data) -> None:...

    @abstractmethod
    def peek(self) -> str:...


class Node:
    def __init__(self, data, pointer = None):
        self.data = data
        self.pointer = pointer

class StackNode(Stack):
    def __init__(self):
        self.head = None # 기준: 헤드로 들어오고 나간다 


    def is_empty(self) -> bool:
        return self.head == None


    def push(self, data) -> None:
        new_node = Node(data, self.head)
        self.head = new_node


    def pop(self) -> str:
        if self.is_empty():
            return "이미 빈 스택입니다."

        pop_data = self.head.data
        self.head = self.head.pointer
        return str(pop_data)


    def delete(self, data) -> None:
        if self.is_empty():
            print("이미 빈 스택입니다.")
            return

        if self.head.data == data:
            self.pop()
            return

        curr_node = self.head
        pre_node = self.head.pointer

        while pre_node is not None:
            if pre_node.data == data:
                curr_node.pointer = pre_node.pointer
                return
            curr_node = pre_node
            pre_node = pre_node.pointer

        print("지울 값이 존재하지 않습니다.")


    def peek(self) -> str:
        if self.is_empty():
            return ""
        else:
            return str(self.head.data)


    def print_stack(self):
        printing_list = []
        start_node = self.head

        while start_node != None:
            printing_list.append(start_node.data)
            start_node = start_node.pointer

        print(printing_list[::-1])



if __name__ == "__main__":
    s = StackNode()
    s.push('A')
    s.print_stack()
    s.push('B')
    s.print_stack()
    s.push('C')
    s.print_stack()
    print(s.peek())
    s.delete('B')
    s.print_stack()
    s.pop()
    s.print_stack()
