def permutations(list):
  result = []
  def backtrack(current_list):
    if len(current_list) == len(list):
      result.append(current_list)
      return
    
    for num in list:
      if num not in current_list:
        current_list.append(num)
        new_list = current_list[:]
        backtrack(new_list)
        current_list.pop()
      else:
        continue

  backtrack([])

  return result
