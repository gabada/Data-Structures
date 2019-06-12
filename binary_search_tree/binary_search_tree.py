from math import inf
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if value < self.value:
      if self.left is None:
        self.left = new_node
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = new_node
      else:
        self.right.insert(value)
    return self

  def contains(self, target):
    current_branch = self
    while current_branch:
      if current_branch.value == target:
        return True
      if current_branch.value > target:
        if current_branch.left != None:
          current_branch = current_branch.left
        else:
          return False
      if current_branch.value < target:
        if current_branch.right != None:
          current_branch = current_branch.right
        else:
          return False

  def get_max(self):
    cur = self
    max = -inf
    while cur != None:
      if cur.value > max:
        max = cur.value
      cur = cur.right
    return max


  def for_each(self, cb):
    pass