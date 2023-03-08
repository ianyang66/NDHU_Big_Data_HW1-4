# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:23:09 2021

@author: USER
"""

import random
ans = random.randint(1,100)
min=1
max=100
cnt=0
def Guess(min,max,cnt):
  if(ans>(min+max)//2):
      min=(min+max)//2
      cnt=cnt+1
      print("1. min: "+str(min) + "  max:  "+str(max))
      Guess(min,max,cnt)
  elif (ans<(min+max)//2):
      max=(min+max)//2
      cnt=cnt+1
      print("2. min: "+str(min) + "  max:  "+str(max))
      Guess(min,max,cnt)
  else:
      cnt=cnt+1
      print("答案為: "+str(ans) + " 一共猜了"+str(cnt)+"次")


Guess(min,max,cnt)
