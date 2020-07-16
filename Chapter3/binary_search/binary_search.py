def binary_search(array, target):
  start = 0
  end = len(array) - 1

  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    
    if array[mid] < target:
      start = mid + 1
    
    if array[mid] > target:
      end = mid - 1
  
  return -1

def recursion_binary_search(array, target, current_index = 0):
  if len(array) == 0:
    return

  mid = (len(array) - 1) // 2

  if array[mid] == target:
    return mid + current_index
  
  if array[mid] > target:
    return recursion_binary_search(array[:mid], target, current_index + mid)
  
  if array[mid] < target:
    return recursion_binary_search(array[mid + 1:], target, current_index)

print(recursion_binary_search([1,2,3,4,5,6], 2))

def find_first_and_last_index(array, target):
  initial_index = binary_search(array, target)
    
  if initial_index == -1:
    return [-1, -1]
    
  lower_index = initial_index
  # lower search
  while lower_index > 0:
    if array[lower_index - 1] == target:
      lower_index -= 1
      continue
    break
    
  upper_index = initial_index
  # upper search
  while upper_index < len(array) - 1:
    if array[upper_index + 1] == target:
      upper_index += 1
      continue
    break
    
  return [lower_index, upper_index]