def rearrange_array_elements(array):
  num1 = ''
  num2 = ''

  array_length = len(array)

  if array_length == 0:
    return 0
  
  # Build a max heap from the array
  for i in range(array_length // 2 - 1, -1, -1):
    heapify(array, array_length, i)
  # We will pull out each element from the heap to build two number that have the largest sum
  max_heap = array[::]

  for i in range(array_length - 1, 0, -1):
    max_heap[0], max_heap[i] = max_heap[i], max_heap[0]
    heapify(max_heap, i, 0)

  while len(max_heap) > 0:
    if len(max_heap) % 2 == 0:
      num1 += str(max_heap.pop())
    else:
      num2 += str(max_heap.pop())

  return [num1, num2]


def heapify(array, array_length, index):
  largest = index
  left_child_index = 2 * index + 1
  right_child_index = 2 * index + 2

  if left_child_index < array_length and array[left_child_index] > array[largest]:
    largest = left_child_index

  if right_child_index < array_length and array[right_child_index] > array[largest]:
    largest = right_child_index

  if largest != index:
    array[largest], array[index] = array[index], array[largest]
    heapify(array, array_length, largest)

rearrange_array_elements([4,6,2,5,9,8])