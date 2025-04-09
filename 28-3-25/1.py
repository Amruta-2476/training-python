class Node:
    def __init__(self,data):     # link yaha nhi aega coz we initialize to None  # non static= jitne objects utne copies
        self.data = data
        self.link = None 
    
    #static can be called using obj as well as class. even if object not created, still iski copy bani rehti hai
    @staticmethod   # means only one copy througout...har object ke liye same copy
    def display_node(s):     # no need for self coz @staticmethod
        if s == None:
            print('No nodes available.')
        else:
            while s!=None:
                print(s.data, end=' ')
                s = s.link

    @staticmethod
    def create_node():
        data = int(input('enter data: '))
        temp = Node(data)
        return temp
    
    @staticmethod
    def insert_at_beginning(s):
        if s==None:
            s = Node.create_node()
        else:
            temp = Node.create_node()
            temp.link = start
            s = temp
        return s
    
    @staticmethod
    def insert_at_end(s):
        if s == None:
            s = Node.create_node()
        else:
            pointer = s
            while pointer.link != None:
                pointer = pointer.link
            pointer.link = Node.create_node()
        return pointer
    
    @staticmethod
    def insert_at_between(s):     # this method is correct, but will fail when duplicate data...so ask index
        if s == None:
            s = Node.create_node()
        else:
            temp = s
            d = int(input('enter data after which to insert node: '))
            while temp.data != d:
                temp = temp.link
            after = temp.link
            temp.link = Node.create_node()   
            temp.link.link = after
        return after    
    
    @staticmethod
    def delete_first(s):
        if s == None:
            print('No nodes in LL')
        else:
            t = s
            s = s.link
            t = None
        return s
        
    
    @staticmethod
    def delete_last(s):
        if s == None:
            print('No nodes in LL')
        elif s.link == None:
            # If only one node exists
            s = None
        else:
            # Traverse to second last node
            curr = s
            while curr.link.link != None:
                curr = curr.link
            # Delete last node
            curr.link = None
        return s
            


start = None
start = Node.insert_at_beginning(start)
start = Node.insert_at_beginning(start)
start = Node.insert_at_beginning(start)
start = Node.insert_at_beginning(start)
# Node.insert_at_end(start)

# Node.insert_at_between(start)
start=Node.delete_first(start)

Node.display_node(start)