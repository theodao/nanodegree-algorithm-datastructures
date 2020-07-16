def selection_sort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp
  
  return array

print(selection_sort([2,1,4,5,9,8]))