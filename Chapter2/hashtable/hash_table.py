class HashTable:
  def __init__(self, size = 100):
    self.array = [None] * 100

  def hash_function(self, key):
    length = len(self.array) + 1
    return hash(key) % length

  def put(self, key, value):
    index = self.hash_function(key)

    if self.array[index] is None:
      self.array[index] = [[key, value]]
      return
    
    if self.array[index] is not None:
      bucket = self.array[index]

      for item in bucket:
        if item[0] == key:
          item[1] = value
          break
      
      bucket.append([key, value])

      return

  def get(self, key):
    index = self.hash_function(key)
    if self.array[index] is None:
      return "Not Found Item with {}".format(key)
    
    if self.array[index] is not None:
      bucket = self.array[index]
      
      for item in bucket:
        if item[0] == key:
          return item[1]
    
    return "Not Found"


  def delete(self, key):
    index = self.hash_function(key)
    if self.array[index] is None:
      return "Not found item with {}".format(key)
    
    if self.array[index] is not None:
      bucket = self.array[index]

      for index, item in enumerate(bucket):
        if item[0] == key:
          bucket.pop(index)
          return
    
    return "Not Found"



hash_table = HashTable()
hash_table.put(1, 2)
hash_table.put(1, 4)
hash_table.put(1, 5)
hash_table.put(2, 6)
print(hash_table.array)