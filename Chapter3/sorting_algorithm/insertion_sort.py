def insertion_sort(array):
  for i in range(1, len(array)):
    key = i
    
    while key > 0 and array[key - 1] > array[key]:
      temp = array[key - 1]
      array[key - 1] = array[key]
      array[key] = temp
      key -= 1
  
  return array

# print(insertion_sort([64,25,12,22,11]))