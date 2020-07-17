def mySqrt(self, x):
  start = 0
  end = x
  
  while start <= end:
    mid = start + (end - start) / 2
    
    if mid * mid <= x and x < (mid + 1) * (mid + 1):
      return mid
    
    if mid * mid > x:
      end = mid
    
    if mid * mid < x:
      start = mid + 1