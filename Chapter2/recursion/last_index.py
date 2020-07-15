def last_index(list, target):
  result = -1

  def helper(list):
    if len(list) == 0:
      return

    for i in range(len(list)):
      if list[i] == target:
        result = i
        helper(list[i + 1::])
      else: continue
  
  helper(list)
  
  return result

last_index([1,2,2,3,4,5], 2)