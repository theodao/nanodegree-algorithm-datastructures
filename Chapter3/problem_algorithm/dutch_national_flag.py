def dutch_national_flag(nums):
  zero_index = 0
  number_two_index = len(nums) - 1
  current_index = 0

  while current_index < number_two_index:
    if nums[current_index] == 0:
      nums[current_index], nums[zero_index] = nums[zero_index], nums[current_index]
      current_index += 1
      zero_index += 1
      continue
    
    if nums[current_index] == 2:
      nums[current_index], nums[number_two_index] = nums[number_two_index], nums[current_index]
      number_two_index -= 1
      continue
      
    if nums[current_index] == 1:
      current_index += 1
  
  return nums