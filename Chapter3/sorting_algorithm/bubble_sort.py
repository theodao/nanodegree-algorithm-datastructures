def bubble_sort(array):
  for i in range(len(array)):
    for j in range(len(array) - 1 - i):
      if array[j] > array[j + 1]:
        temp = array[j + 1]
        array[j + 1] = array[j]
        array[j] = temp
  
  return array

print(bubble_sort([64,25,12,22,11]))
