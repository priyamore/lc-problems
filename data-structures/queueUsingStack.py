'''
Problem 1:
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.'''

#Solution 1:
class MyQueue:

    def __init__(self):
        self.stack=[]
        self.i=0

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        return self.stack.pop(self.i)
        self.i += 1 

    def peek(self) -> int:
        return self.stack[self.i]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()