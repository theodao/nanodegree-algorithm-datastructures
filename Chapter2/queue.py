class Queue:
  def __init__(self):
    self.list = []

  def size(self):
    return len(self.list)

  def dequeue(self):
    if (self.size == 0):
      return "Queue is empty"

    return self.list.pop(0)

  def enqueue(self, value):
    self.list.append(value)

    return value

class Stack:
  def __init__(self):
    self.list = []
  
  def size(self):
    return len(self.list)
  
  def push(self, value):
    self.list.append(value)

    return value
  
  def pop(self):
    if (self.size() == 0):
      return None

    return self.list.pop()

class QueueUsingStack:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()
  
  def enqueue(self, value):
    self.stack1.push(value)
  def dequeue(self, value):
    if self.stack2.size() == 0:
      while self.stack1.size != 0:
        self.stack2.push(self.stack1.pop())
    return self.stack2.pop()
        
