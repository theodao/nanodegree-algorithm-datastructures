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

def balanced_parenthesis(str):
  stack = Stack()
  trimmed_str = str.replace(' ', '')

  for letter in trimmed_str:
    if letter == '(':
      stack.push(letter)
    
    if letter == ')':
      value = stack.pop()

      if (value == None):
        return False
  
  return stack.size() == 0

def minimum_bracket_reversal(str):
  stack = Stack()

  for letter in str:
    if letter == '{':
      stack.push(letter)
    
    if letter == '}':
      value = stack.pop()

      if (value == None):
        stack.push(letter)

  return len(stack.list) / 2

def polish_notation(tokens):
  stack = []

  for letter in tokens:
    if (letter.isnumeric()):
      stack.append(letter)
    else:
      operator = letter
      num1 = int(stack.pop())
      num2 = int(stack.pop())
      result = None
      
      if operator == '+':
        result = num1 + num2
      elif operator == '-':
        result = num2 - num1
      elif operator == '*':
        result = num1 * num2
      else:
        result = num2 / num1
      stack.append(result)

  return stack.pop()


print(minimum_bracket_reversal("}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{"))