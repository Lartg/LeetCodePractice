def myPow(x, n): 
  base = 1
  if n == 0:
      return base
  else:
      answer = base
      for pow in range(n):
          answer = answer*x
      if n > 0: 
          return answer
      elif n < 0:
          print(answer)
          answer = 1/answer
          return answer

print(myPow(2,-4))