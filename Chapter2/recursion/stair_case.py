def stair_case(n):
  if n == 0:
    return 1
  
  if n == 1:
    return 1

  if n == 2:
    return 2
  
  return stair_case(n - 1) + stair_case(n - 2) + stair_case(n - 3)


print(stair_case(7))
