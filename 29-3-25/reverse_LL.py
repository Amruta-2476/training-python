# reverse the Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

    @staticmethod
    def display_node(s):
        if s is None:
            print("No nodes available.")
        else:
            index = 0
            while s is not None:
                print(f"{s.data}", end="| ")
                s = s.link
                index += 1
            print("None")

    @staticmethod
    def create_node():
        data = int(input("Enter data: "))
        return Node(data)
    
    @staticmethod
    def insert_at_end(s):
        if s is None:
            s = Node.create_node()
        else:
            pointer = s
            while pointer.link is not None:
                pointer = pointer.link
            pointer.link = Node.create_node()
        return s
    
    @staticmethod
    def reverse_the_LL(s):
        pre = None
        temp = s
        while temp is not None:
            next = temp.link
            temp.link = pre
            pre = temp
            temp = next
        return pre
    


start = None
start = Node.insert_at_end(start)
start = Node.insert_at_end(start)
start = Node.insert_at_end(start)

start = Node.reverse_the_LL(start)

Node.display_node(start)
