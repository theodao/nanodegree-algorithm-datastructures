def search_in_rotated_array(nums, target):
  if len(nums) == 0:
    return -1

  # Find the index of the minimum number
  start = 0
  end = len(nums) - 1
  
  while start < end:
    mid = start + (end - start) // 2
    
    if nums[mid] > nums[end]:
      start = mid + 1
    
    if nums[mid] < nums[end]:
      end = mid
  
  if nums[start] == target:
    return start
  
  # We have the smallest number index here
  smallest_number_index = start
  start = 0
  end = len(nums) - 1
  
  # If the target in range of smallest number to the end
  if nums[smallest_number_index] <= nums[end] and target <= nums[end]:
    start = smallest_number_index
  # Target in range of the rotated part
  else:
    end = smallest_number_index
    
  while start <= end:
    mid = start + (end - start) // 2
    
    if nums[mid] == target:
      return mid
    
    if nums[mid] > target:
      end = mid - 1
    
    if nums[mid] < target:
      start = mid + 1
  
  return -1