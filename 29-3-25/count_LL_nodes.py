# count no.of nodes in LL

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
    def count_no_of_nodes(s):
        count = 0
        while s is not None:
            count += 1
            s = s.link
        return count
    


start = None
start = Node.insert_at_end(start)
start = Node.insert_at_end(start)
start = Node.insert_at_end(start)

Node.display_node(start)

count = Node.count_no_of_nodes(start)  
print(f"Total number of nodes: {count}")