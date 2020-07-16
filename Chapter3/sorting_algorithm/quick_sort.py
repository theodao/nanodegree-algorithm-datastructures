def quick_sort(array, low, high):
  if low < high:
    index = partition(array, low, high)
    quick_sort(array, low, index - 1)
    quick_sort(array, index + 1, high)
  
  return array

def partition(array, low, high):
  pivot = array[high]
  pointer1 = low
  pointer2 = high - 1

  while pointer1 <= pointer2:
    while array[pointer1] < pivot:
      pointer1 += 1
      
    
    while array[pointer2] > pivot:
      pointer2 -= 1

    if (pointer1 <= pointer2):
      array[pointer1], array[pointer2] = array[pointer2], array[pointer1]
  
  array[pointer1], array[high] = array[high], array[pointer1]

  return pointer1

arr = [10, 7, 8, 9, 1, 5]

print(quick_sort(arr, 0, len(arr) - 1))
    
