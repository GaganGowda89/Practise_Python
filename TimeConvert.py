#!/usr/bin/python

def TimeConvert(num):
  """ Convert the given number to Time format ("Hour":"Min")
  
  Args:
  num(int): Takes input parameter
  
  Returns:
  str: "hour":"min"
  """
  if(num!=0  or num<=60):
    hour = num / 60
    num = num % 60
    hour = hour + 0
  return str(hour)+":"+str(num)
