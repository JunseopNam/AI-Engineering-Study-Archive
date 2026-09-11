# single_linked_list 구현하기

class Node:
    def __init__(self, data, pointer = None):
        self.data = data
        self.pointer = pointer


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def add(self, *args):
        for data in args:
            new_node  = Node(data, None)
            if self.head == None:
                self.head = new_node
                self.tail = self.head
                self.count = 1
            else:
                self.tail.pointer = new_node
                self.tail = new_node
                self.count += 1


    def insert(self, position : int, data):
        new_node = Node(data, None)
        start_node = self.head

        if self.count == 0:
            self.head = new_node
            self.tail = self.head
            self.count = 1
            return

        if position == 1:
            new_node.pointer = start_node
            self.head = new_node
            self.count += 1
            return

        if position == (self.count + 1):
            self.tail.pointer = new_node
            self.tail = new_node
            self.count += 1
            return

        if 1 < position and position < (self.count + 1):
            for _ in range(position - 2):
                start_node = start_node.pointer
        else:
            print("범위 밖입니다.")
            return

        new_node.pointer = start_node.pointer
        start_node.pointer = new_node
        self.count += 1


    def reverse(self):
        prev_node = None
        start_node = self.head
        self.tail = self.head

        while start_node is not None:
            next_node = start_node.pointer
            start_node.pointer = prev_node
            prev_node = start_node
            start_node = next_node
        self.head = prev_node
            

    def remove(self):
        start_node = self.head

        if self.count == 0:
            return

        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
            return
        
        while start_node.pointer != self.tail:
            start_node = start_node.pointer

        self.tail = start_node
        start_node.pointer = None
        self.count -= 1



    def node_print(self):
        printing_list = []
        start_node = self.head

        while start_node != None:
            printing_list.append(start_node.data)
            start_node = start_node.pointer

        print(printing_list)


if __name__ == "__main__":
    s = SingleLinkedList()
    s.add(1,3,7)
    s.node_print()
    s.insert(3,5)
    s.node_print()
    s.reverse()
    s.node_print()
    s.remove()
    s.node_print()