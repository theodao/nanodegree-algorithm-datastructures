class LRUCache(object):

  def __init__(self, capacity):
      """
      :type capacity: int
      """
      self.capacity = capacity
      self.hash_table = {}
      self.size = 0
      self.doubly_linkedlist = DoublyLinkedList()


  def get(self, key):
      """
      :type key: int
      :rtype: int
      """
      found_item = self.hash_table.get(key)
      
      if found_item is not None:
        self.doubly_linkedlist.move_to_head(found_item)
        return found_item.value
      
      if found_item is None:
        return -1
        

  def put(self, key, value):
      """
      :type key: int
      :type value: int
      :rtype: None
      """
      found_item = self.hash_table.get(key)
      
      if found_item is not None:
        self.hash_table.get(key).value = value
        self.doubly_linkedlist.move_to_head(found_item)
        return
      
      new_node = Node(key, value)
      print(new_node)
      if found_item is None:
        if self.size < self.capacity:
          self.size += 1
        else:
          key_to_remove = self.doubly_linkedlist.remove_tail()
          del self.hash_table[key_to_remove]
        self.hash_table[key] = new_node
        self.doubly_linkedlist.insert_head(new_node)
      
class Node(object):
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.previous = None
      
class DoublyLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def move_to_head(self, node):
    if self.head == node:
      return
    
    if node == self.tail:
      node.previous.next = None
      self.tail = node.previous
      node.previous = None
      node.next = self.head
      self.head.previous = node
      self.head = node
      return
    
    node.previous.next = node.next
    node.next.previous = node.previous
    node.next = self.head
    self.head.previous = node
    node.previous = None
    
    self.head = node
    
  def insert_head(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
      return
    
    if self.head is not None:
      node.next = self.head
      self.head.previous = node
      self.head = node
    
  def remove_tail(self):
    tail = self.tail
    
    if self.tail == self.head:
      self.tail = None
      self.head = None
    else:
      self.tail.previous.next = None
      self.tail = self.tail.previous
    
    return tail.key
