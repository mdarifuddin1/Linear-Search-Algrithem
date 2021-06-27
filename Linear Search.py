# Happy coding ,code by Md Arif uddin
# This example of linear Search code 
# coding time 1:17 Am ,date 6/28/2021

pos = -1
list = [12,34,2,4,5,6]
n = 2  # if you change value of n our output will be changed 

def Search(list, n):

  i = 0

  while i < len(list):
    if list[i] == n:
      globals() ['pos'] = i
      return True
    i = i+1
  return False

if Search(list, n):
  print("Found value of : ",pos)
else:
  print("Not Found")


# Right now my output is , Found value of : 2
