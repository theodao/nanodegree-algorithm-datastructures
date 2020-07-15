import hashlib


def calc_hash():
  sha = hashlib.sha256()

  hash_str = "We are going to encode this string of data!".encode('utf-8')

  sha.update(hash_str)

  return sha.hexdigest()

class Block:
  def __init__(self, data, previous_hash):
    self.data = data
    self.previous_hash = previous_hash
    self.hash = calc_hash()

class BlockChain:
  def __initi__(self, head):
    self.tail = None
  
  def append(self, data):
    if self.tail is None:
      self.tail = Block(data, None)
      return
    
    if self.tail is not None:
      self.tail = Block(data, self.tail)

  def search(self, data):
    if self.tail is None:
      return None
    
    if self.tail is not None:
      current_block = self.tail

      while current_block:
        if current_block.data == data:
          return current_block
        else:
          current_block = current_block.previous_hash
      
      return None