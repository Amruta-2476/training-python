# insert at first, deletion from first
# implement stack using linked list (do this later)

'''
Problem 1: Undo Feature using Stack 
Problem Statement: Implement the "undo" feature in a text editor. Every time a user types something, it gets pushed onto the stack. When the user presses "undo," the last operation is undone (popped from the stack). 
'''
class Stack:
    def __init__(self):
        self.mystack = []
    def push(self, val):
        self.mystack.append(val)
        print(f'Pushed {val} on text editor.')
    def pop(self):
        if len(self.mystack) == 0:
            print('Test editor empty. Cannot undo')
        else:
            popped_val = self.mystack.pop()
            print(f'Popped {popped_val} from stack.')
    def display(self):
        print(self.mystack,' is the text editor.')

ob = Stack()
while True:
    print('1. user input: ')
    print('2. undo: ')
    print('3. display: ')
    print('4. exit: ')
    ch = int(input('enter your choice: '))
    if ch == 1:
        val = input('enter a character: ')
        ob.push(val)
    elif ch == 2:
        ob.pop()
    elif ch == 3:
        ob.display()
    elif ch == 4:
        print('exiting . . .')           
        break
    else:
        print('invalid choice')
        