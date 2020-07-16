def merge_sort(array, start, end):
  if start < end:
    mid = (start + end) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)
    merge(array, start, mid, end)

def merge(array, start, mid ,end):
  left_array = [None] * (mid - start + 1)
  right_array = [None] * (end - mid)
  m = 0
  n = 0
  array_index = start

  for i in range(0, mid - start + 1):
    left_array[i] = array[start + i]

  for j in range(0, end - mid):
    right_array[j] = array[mid + j + 1]

  while m < mid - start + 1 and n < end - mid:
    if left_array[m] < right_array[n]:
      array[array_index] = left_array[m]
      m += 1
      array_index += 1
      continue
    if right_array[n] < left_array[m]:
      array[array_index] = right_array[n]
      n += 1
      array_index += 1
      continue
  
  while  m < len(left_array):
    array[array_index] = left_array[m]
    m += 1
    array_index += 1
  
  while n < len(right_array):
    array[array_index] = right_array[n]
    n += 1
    array_index += 1


arr = [2,1,4,5,9]

merge_sort(arr, 0, 4)

print(arr)

# arr = [None] * 10
# arr[0] = 1
