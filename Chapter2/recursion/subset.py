def subset(nums):
  result = [[]]

  def backtrack(current, index):
      for i in range(index, len(nums)):
          current.append(nums[i])
          result.append(current[:])
          backtrack(current[:], i + 1)
          current.pop()
  backtrack([], 0)
  return result
