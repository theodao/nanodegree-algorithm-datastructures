class Group(object):
  def __init__(self, _name):
    self.name = _name
    self.groups = []
    self.users = []

  def add_group(self, group):
    self.groups.append(group)

  def add_user(self, user):
    self.users.append(user)

  def get_groups(self):
    return self.groups

  def get_users(self):
    return self.users

  def get_name(self):
    return self.name


def is_user_in_group(user, group):
  global is_user
  is_user = False
  """
  Return True if user is in the group, False otherwise.

  Args:
    user(str): user name/id
    group(class:Group): group to check user membership against
  """

  def helper(user, group):
    if user in group.get_users():
      global is_user
      is_user = True
    else:
      if len(group.get_groups()) == 0:
        return

      for group in group.get_groups():
        helper(user, group)
  
  helper(user, group)

  return is_user



parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child_2.add_user(sub_child_user)

child.add_group(sub_child)
child.add_group(sub_child_2)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))

# print(is_user)