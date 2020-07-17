def max_and_min_unsorted(nums):
  max = -float('inf')
  min = float('inf')

  for num in nums:
    if num > max:
      max = num
    if num < min:
      min - num
  
  return (min, max)