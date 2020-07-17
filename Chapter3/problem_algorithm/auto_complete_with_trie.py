class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end = False

  def suffix(self, suffix = ''):
    result = []

    for char in self.children:
      children_node = self.children[char]

      if children_node.is_end:
        result.append(suffix)
      
      if children_node.children:
        result.extend(children_node.suffix(suffix + char))

    return result

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    current_node = self.root
    # print(current_node)
    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      current_node = current_node.children[char]
    current_node.is_end = True

  def search(self, prefix):
    current_node = self.root

    for char in prefix:
      if char not in current_node.children:
        return False
      current_node = current_node.children[char]
    
    return current_node
      
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
  MyTrie.insert(word)

result = MyTrie.search('ant')
print(result.suffix())
