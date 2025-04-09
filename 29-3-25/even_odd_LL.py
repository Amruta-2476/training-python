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
    def even(s):
        current = s
        while current:
            if current.data %2 == 0:
                return current.data
    


start = None
start = Node.insert_at_end(start)
start = Node.insert_at_end(start)
start = Node.insert_at_end(start)

Node.display_node(start)
Node.even(start)

Node.display_node(start)

