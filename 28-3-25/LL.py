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
    def insert_at_beginning(s):
        temp = Node.create_node()
        temp.link = s
        return temp

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
    def insert_at_between(s, index):
        if index < 1:
            print('Invalid index')
            return s
        elif index == 1:
            return Node.insert_at_beginning(s)
        else:
            temp = s
            for i in range(index - 2):  # Navigate to the node before the index
                if temp is None or temp.link is None:
                    print('Index out of bound')
                    return s
                temp = temp.link
            new_node = Node.create_node()
            new_node.link = temp.link
            temp.link = new_node
            return s

    @staticmethod
    def delete_first(s):
        if s is None:
            print("No nodes in LL")
            return None
        return s.link

    @staticmethod
    def delete_last(s):
        if s is None:
            print("No nodes in LL")
            return None
        elif s.link is None:
            return None
        else:
            curr = s
            while curr.link.link is not None:
                curr = curr.link
            curr.link = None
        return s

    @staticmethod
    def delete_from_between(s, index):
        if s is None:
            print("No nodes in LL")
            return s

        if index < 1:
            print("Invalid index")
            return s

        if index == 1:
            return Node.delete_first(s)

        temp = s
        for i in range(index - 2):  # Navigate to the node before the index
            if temp is None or temp.link is None:
                print("Index out of bound")
                return s
            temp = temp.link

        if temp.link is None:
            print("Index out of bound")
            return s

        temp.link = temp.link.link  # Remove the node by skipping it
        return s

    @staticmethod
    def count_no_of_nodes(s):
        count = 0
        while s is not None:
            count += 1
            s = s.link
        return count


# Menu-driven program
def menu():
    start = None
    while True:
        print("\n----- Linked List Menu -----")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert in Between (After Index)")
        print("4. Delete First Node")
        print("5. Delete Last Node")
        print("6. Delete in Between (Particular Index)")
        print("7. Display")
        print("8. Count Number of Nodes")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            start = Node.insert_at_beginning(start)
        elif choice == 2:
            start = Node.insert_at_end(start)
        elif choice == 3:
            index = int(input("Enter index after which to add node: "))
            start = Node.insert_at_between(start, index)
        elif choice == 4:
            start = Node.delete_first(start)
        elif choice == 5:
            start = Node.delete_last(start)
        elif choice == 6:
            index = int(input("Enter index from which to delete node: "))
            start = Node.delete_from_between(start, index)  # FIXED: Update start
        elif choice == 7:
            Node.display_node(start)
        elif choice == 8:
            count = Node.count_no_of_nodes(start)  
            print(f"Total number of nodes: {count}")
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
