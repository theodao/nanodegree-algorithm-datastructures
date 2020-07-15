class Node:
  def __init__(self, value = None):
    self.left = None
    self.right = None
    self.value = value

class Binary_Search_Tree:
  def __init__(self, root = None):
    self.root = root
  
  def insert(self, value):
    new_node = Node(value)
    current_node = self.root

    if current_node == None:
      self.root = new_node
      return
    
    while True:
      if value < current_node.value:
        if current_node.left != None:
          current_node = current_node.left
          continue
        else:
          current_node.left = new_node
          break
      if value > current_node.value:
        if current_node.right != None:
          current_node = current_node.right
          continue
        else:
          current_node.right = new_node
          break
      break
  
  def search(self, value):
    current_node = self.root

    def helper(r):
      if r == None:
        return False
      
      if r.value == value:
        return True
      
      if r.value > value:
        return helper(r.left)

      if r.value < value:
        return helper(r.right)

    return helper(current_node)
          

  def delete(self, value):
    def find_min(r):
      current = r
      while (current.left != None):
        current = current.left
      
      return current
    
    def helper(r, value):
      if r == None:
        return None
      
      if r.value < value:
        r.left = helper(r.left, value)
      
      if r.value > value:
        r.right = helper(r.right, value)

      if r.value == value:
        if r.left == None:
          return r.right
        
        if r.right == None:
          return r.left

        if r.left != None and r.right != None:
          min_node = find_min(r.right)
          r.value = min_node.value
          r.right = helper(r.right, min_node.value)
    
    helper(self.root, value)

    

      
  def tree_traversal(self):
    result = []

    def helper(r):
      if r == None:
        return
      result.append(r.value)
      helper(r.left)
      helper(r.right)
    
    helper(self.root)
    return result

tree = Binary_Search_Tree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(4)
tree.insert(5)
print(tree.delete(2))
# print(tree.search(9))
# print(tree.tree_traversal())
      
    