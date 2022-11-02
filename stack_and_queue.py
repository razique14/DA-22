# -*- coding: utf-8 -*-
"""Stack  and Queue

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A99N5x0Ppt6AR6TT1hpXNbhEA0I99XyT
"""



"""Stack (LIFO/FILO)"""

A = []
A.append(1) #[1]
A.append(2) #[1,2]
A.append(3) #[1,2,3]
A.append(4) #[1,2,3,4]
A.append(5) #[1,2,3,4,5]
print(A)
A.pop() #[1,2,3,4]
A.pop() #[1,2,3]
A.pop() #[1,2]
A.pop() #[1]
A.pop() #[]]
print(A)

"""The above process is not preferrable for higher data because of operation complexity as Lists are dynamic arrays.

Hence, Dequeues are used. Dequeues are generalization of stacks and queues. They are built using doubly linked lists. It allocates memory only when needed.
"""

from collections import deque
stack = deque()
dir(stack)

stack.append(3)

stack[-1]

stack.pop()

"""Python implementation of prototype of dequeue:"""

class Stack:
  def __init__(self):
    self.data = deque()
  
  def push(self,val):
    return self.data.append(val)
  
  def pop(self):
    return self.data.pop()
  
  def latest(self):
    return self.data[-1]
  
  def isempty(self):
    # if (len(self.data) == 0):
    #   return 'Stack is empty'
    return (len(self.data) == 0)
  
  def length(self):
    return len(self.data)
    
  def display(self):
    return self.data

s = Stack()

# s.isempty()
# s.push(2)
# s.push(3)
# s.push(4)
# s.pop()
# s.pop()
# s.display()

s.length()

a = []
def d(a):
  return (len(a) == 0)

d(a)

"""
Queue (FIFO)

"""

A = []
A.insert(0,1) #[1]
A.insert(0,2) #[1,2]
A.insert(0,3) #[1,2,3]
A.insert(0,4) #[1,2,3,4]
A.insert(0,5) #[1,2,3,4,5]
print(A)
A.pop() #[1,2,3,4]
A.pop() #[1,2,3]
A.pop() #[1,2]
A.pop() #[1]
A.pop() #[]]
print(A)

from collections import deque
que = deque()

que.appendleft(1)

que.pop()

class Queue:
  def __init__(self):
    self.data = deque()
  
  def push(self,val):
    # return self.data.insert(0,val)
    return self.data.appendleft(val)
  
  def pop(self):
    return self.data.pop()
  
  def latest(self):
    return self.data[0]
  
  def isempty(self):
    # if (len(self.data) == 0):
    #   return 'Stack is empty'
    return (len(self.data) == 0)
  
  def length(self):
    return len(self.data)
    
  def display(self):
    return self.data

q = Queue()

q.display()

q.push(1)

q.pop()

example = Queue()

example.push({'name':'kaif','height':5, 'weight':50})
example.push({'name':'razique','height':5.5, 'weight':60})
example.push({'name':'moeen','height':5.2, 'weight':80})

# example.display()
example.latest()['weight']