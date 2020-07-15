def huffman_coding(str):
  frequency = {}
  sorted_frequency = []
  codes = {}

  # Frequency of character in a string
  for char in str:
    if frequency.get(char) is not None:
      frequency[char] = frequency[char] + 1
    else:
      frequency[char] = 1
  
  # Sort the frequency of character in a string
  for key in frequency:
    sorted_frequency.append([frequency[key], key])
  
  sorted_frequency = sorted(sorted_frequency)

  # Building a tree based on sorted frequency
  while len(sorted_frequency) > 1:
    two_least_small = [sorted_frequency[0][1], sorted_frequency[1][1]]
    remaining_sorted_frequency = sorted_frequency[2::]
    combining_frequency = sorted_frequency[0][0] + sorted_frequency[1][0]

    sorted_frequency = remaining_sorted_frequency
    item = [combining_frequency, two_least_small]
    sorted_frequency.append(item)
    sorted_frequency.sort()
  
  # Built Tree
  built_tree = sorted_frequency[0][1]

  # Assigning code for character
  def assign_code(node, code):
    if type(node) == type(''):
      codes[node] = code
      return
    else:
      assign_code(node[0], code + '0')
      assign_code(node[1], code + '1')
  assign_code(built_tree, '')
  
  # Encode
  def encode(str):
    result = ''

    for char in str:
      result += codes[char]
    
    return result

  encoded_string = encode(str)

  # Decode
  def decode(encoded_string):
    result = ''
    temp_tree = built_tree

    for code in encoded_string:
      if code == '0':
        temp_tree = temp_tree[0]
      
      if code == '1':
        temp_tree = temp_tree[1]
      
      if type(temp_tree) is type(''):
        result += temp_tree
        temp_tree = built_tree
    
    return result
      

  decoded_string = decode(encoded_string)

  print(encoded_string)
  print(decoded_string)




huffman_coding("aaabccdeeeeeffg")
