#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
  num = []
  for i in range (x):
    try:
      num.append(my_list[i])
    except:
      break
  return num 
