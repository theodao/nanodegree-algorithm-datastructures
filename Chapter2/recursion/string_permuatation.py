def string_permutation(str):
  result = []
  list_string = list(str)
  
  def backtrack(current):
    if len(current) == len(str):
      result.append(current[:])
      return
    for i in range(len(list_string)):
      if list_string[i] not in current:
        current.append(list_string[i])
        backtrack(current[:])
        current.pop()
      else: continue
  backtrack([])
  
  return map(lambda list: ''.join(list), result)
      