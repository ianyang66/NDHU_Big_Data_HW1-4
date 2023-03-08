# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:23:12 2021

@author: USER
"""
import random
amount=80
A=5
B=5
C=10
D=20
E=40
award=[]
list=[]

good=[]

def SetUpTicketDistri(): 
    for i in range(A):
        award.append("A")
    for i in range(B):
        award.append("B")
    for i in range(C):
        award.append("C")
    for i in range(D):
        award.append("D")
    for i in range(E):
        award.append("E")

    random.shuffle(award)
    
    for i in range (amount):
        list.append (award[i])
        
def DisplayTicketIntro():

    print("====================")
    print("One Price 一番賞開抽")
    print("====================")
    print("一番賞剩餘數量: "+ str(amount))
    print("剩餘號碼： \n")
    for i in range(amount):
        if list[i]!="F":
            print (i+1, end = '　')    
            
def ChoosePlayType():
   buy=1
   while buy!=-1:
      buy= int(input("購買方式，自行選購請按1，電腦選購請按2，離開請按-1")) 
      if (list[buy]=="F"):
          print("已賣出 \n")
          break
      good.append(list[buy-1])
      list[buy-1]="F"
      
SetUpTicketDistri()  
DisplayTicketIntro()
ChoosePlayType()
 

"""    
SetUpTicketDistri()

ChoosePlayType()
Banpresto()
"""