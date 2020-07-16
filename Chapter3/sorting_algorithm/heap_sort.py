def heap_sort(arr):
  array_length = len(arr)

  # Build max heap from the array
  for i in range(array_length / 2 - 1, -1, -1):
    heapify(arr, array_length, i)

  # Extract element from the heap
  for i in range(array_length - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
  
  return arr

def heapify(arr, array_length, index):
  largest = index
  left_child_index = 2 * index + 1
  right_child_index = 2 * index + 2

  if left_child_index < array_length and arr[left_child_index] > arr[largest]:
    largest = left_child_index

  if right_child_index < array_length and arr[right_child_index] > arr[largest]:
    largest = right_child_index

  if largest is not index:
    arr[index], arr[largest] = arr[largest], arr[index]
    heapify(arr, array_length, largest)


print(heap_sort([12,11,13,5,6,7]))