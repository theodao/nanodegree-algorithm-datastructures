def reverse_string(s):
  result = ""

  for i in range(len(s)):
    result += s[len(s) - i - 1]
  
  return result

def anagram_check(str1, str2):
  filtered_string1 = str1.replace(" ", "").lower()
  filtered_string2 = str2.replace(" ", "").lower()

  return sorted(filtered_string1) == sorted(filtered_string2)

def hamming_distance(str1, str2):
  count = 0

  for i in range(len(str1)):
    if (str1[i] != str2[i]):
      count += 1

  return count

def word_flipper(str):
  word_list = str.split(' ')

  for i in range(len(word_list)):
    word_list[i] = word_list[i][::-1]

  return " ".join(word_list)
