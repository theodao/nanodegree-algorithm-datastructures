class Node:
  def __init__(self, value):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    new_node = Node(value)

    # If the head is None
    if (self.head == None):
      self.head = new_node
      return
    
    # else
    current_node = self.head

    while (current_node):
      current_node = current_node.next
    
    current_node.next = new_node
    return
  
  def removeAtIndex(self, index):
    current_node = self.head
    count = 0

    if (self.head == None):
      return

    if (index == 0):
      self.head = self.head.next
      return

    while (current_node and count < index):
      count += 1
      current_node = current_node.next
    
    current_node.next = current_node.next.next
    return


  # Print out the list of values of the linked list
  def print_out_value(self):
    node_list = []
    current_node = self.head

    while (current_node):
      node_list.append(current_node.value)
      current_node = current_node.next
    
    print(node_list)

  

# Reverse a linked list
def reverse_list(self, head):
  previous_node = None
  current_node = head
  next_node = None
  
  while current_node != None:
    next_node = current_node.next
    current_node.next = previous_node
    previous_node = current_node
    current_node = next_node
  
  return previous_node

# Detect a loop
def detect_loop(self, head):
  if head == None or head.next == None:
    return False
  
  slow = head
  fast = head.next

  while slow != fast:
    if (slow == None or fast == None):
      return False
    
    slow = slow.next
    fast = fast.next.next
  
  return True
  