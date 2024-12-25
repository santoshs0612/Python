# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(4))

def fibonacci(n):
  
  count=1
  n1=0,
  n2 =1
  print(0)
  nextNum =n2
  while count<=n:
    print(nextNum)
    count=count+1
    n1,n2 = n2,nextNum
    nextNum = n1+n2

fibonacci(4)