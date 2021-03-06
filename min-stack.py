class MinStack:

  def __init__(self):
    self.stack = []
    self.min = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    if len(self.min) == 0:
      self.min.append(val)
    elif self.min[-1] >= val:
      self.min.append(val)

  def pop(self) -> None:
    if self.stack[-1] == self.min[-1]:
      self.min.pop()
    self.stack.pop()
        

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min[-1]
        