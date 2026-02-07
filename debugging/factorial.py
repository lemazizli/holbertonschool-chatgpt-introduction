#!/usr/bin/python3
import sys
def factorial(n):
  if n<0:
    return 0
  result = 1
  while n>1:
    result *=n
    n-=1
  return result
if len(sys.argv)>1:
  try:
    n = int(sys.argv[1])
    print(factorial(n))
  except ValueError:
    print("Please enter a valid integer")
  
