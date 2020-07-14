def reverse_string(str):
  if str == '':
    return ''
  
  return str[-1] + reverse_string(str[0:-1])
