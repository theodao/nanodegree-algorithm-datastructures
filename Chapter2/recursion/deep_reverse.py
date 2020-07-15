def deep_reverse(list):
  if len(list) == 0:
    return list
  result = []
  list = list[::-1]
  def helper(l):
    if type(l) is not list:
      result.append(l)

deep_reverse([1,2,3,4,5])
