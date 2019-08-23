class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.storage == [None]*self.capacity:
      self.storage = []
      self.storage.append(item)
      print(self.storage)
    elif len(self.storage) < self.capacity: 
      self.current = 321
      self.storage.append(item)
      print(self.storage)
    elif len(self.storage) == 3:
      if self.current == 321:
        self.current = 132
        self.storage[0] = item
        print(self.storage)
      elif self.current == 132:
        self.current = 213
        self.storage[1] = item
        print(self.storage)
      elif self.current == 213:
        self.current = 321
        self.storage[2] = item
        print(self.storage)


  def get(self):
    print("hi")
    # return items in storage. 
    # if an item is None, ignore the none and only print the []
    # if one item is in 
    if self.storage == [None]*self.capacity:
      print([])
    else:
      print(self.storage)



buffer = RingBuffer(3)

buffer.get()
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')