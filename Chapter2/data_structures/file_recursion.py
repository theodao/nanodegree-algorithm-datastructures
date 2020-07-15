import os

def finding_file(suffix, path):
  result = []
  path = os.getcwd() + '/testdir'
  def find_file(suffix, path):
    for item in os.listdir(path):
      if os.path.isfile(path + '/' + item) and item.endswith(suffix):
        result.append(item)
      
      if os.path.isdir(path + '/' + item):
        find_file(suffix, path + '/' + item)
    return
  find_file(suffix, path)

  return result

# print(finding_file('.h', os.getcwd() + '/testdir'))