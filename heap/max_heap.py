class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) - 1
    self._bubble_up(index)

  def delete(self):
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    del_val = self.storage.pop(-1)
    self._sift_down(0)
    return del_val


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # keep bubbling up until we've either reached the top of the heap 
    # or we've reached a point where the parent is higher priority
    while index > 0:
      # on a single bubble up iteration:
      # get the parent index
      parent = (index - 1) // 2
      # compare the child value against the value of parents
      # if the child value is higher priority than its parents
      if self.storage[index] > self.storage[parent]:
        # swap them
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # update the childs index to be the new index it is now at
        index = parent
      # otherwise, child is at a valid spot
      else:
      # stop bubbling up
        break

  def _sift_down(self, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    largest = index
    if len(self.storage) > left and self.storage[largest] < self.storage[left]:
      largest = left
    if len(self.storage) > right and self.storage[largest] < self.storage[right]:
      largest = right
    if largest != index:
      self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
      self._sift_down(largest)