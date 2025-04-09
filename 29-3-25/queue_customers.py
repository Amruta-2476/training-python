'''
Problem 2: Waiting Line Simulation using Queue 
Problem Statement: Simulate a waiting line at a bank using a queue. The bank serves the first customer in line (FIFO-First In First Out). Implement a simple queue system where customers join the line and the bank serves them in the order they arrived. 
'''

class Queue:
    def __init__(self):
        self.myqueue = []
    def enqueue(self,val):
        self.myqueue.append(val)
        print(f'Added {val} in queue.')

    def dequeue(self):
        if self.isEmpty():
            print('Queue empty. Cannot pop')
        else:
            dequeue_val = self.myqueue.pop(0)
            print(f'Removed {dequeue_val} from queue.')
        
    def show(self):
        print(self.myqueue,' is the queue.')