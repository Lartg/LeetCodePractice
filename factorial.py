class Solution:
  def __init__(self):
      self.answer = 1


  def factorial(self, int):
    
    self.answer = self.answer * int

    if int > 1:
      nextInt = int - 1
      self.factorial(nextInt)
    else:
      return print(self.answer)

solution = Solution()

solution.factorial(4)