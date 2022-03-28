'''

In: string
Out: bool

Intuition:
check if string is a palindrome - spelled same way forwards and back

psuedocode:
normalize string
reverse order of string
check reverse order against original
return bool

'''
from string import punctuation
class Solution():
  def isPalindrome(self, string: str) -> bool:
    operational_string = list(string.lower().replace(' ', '').translate(str.maketrans('', '', punctuation)))
    check_string = list(reversed(operational_string))
    if operational_string == check_string:
      return True
    return False
    

solution = Solution()
print(solution.isPalindrome('race, car'))