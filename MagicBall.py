# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:04:21 2021

@author: USER
"""
import random
from random import choice

Good = [123,456,789,147,258,369,159,357]
boardA=["*"]*10
boardC=["*"]*10
def MagicBall(playtimes):
    win=0
    loss=0
    for i in range(playtimes):
        ListC=choice(Good)
        NumC= int(ListC)
        ListA = random.sample(range(1,9),3)
        ListA.sort()
        list_new = [str(x) for x in ListA]
        strA= "".join(list_new)  
        NumA= int(strA)
        NumC= int(ListC)
    
        boardA[NumA//100]="O"
        boardA[(NumA%100)//10]="O"
        boardA[NumA%10]="O"
    
        boardC[NumC//100]="O"
        boardC[(NumC%100)//10]="O"
        boardC[NumC%10]="O"
        print (str(i)+". 本次目標")
        print (boardC[1:4] ,end='\n')
        print (boardC[4:7] ,end='\n')
        print (boardC[7:10] ,end='\n')
        print ("本次結果")
        print (boardA[1:4] ,end='\n')
        print (boardA[4:7] ,end='\n')
        print (boardA[7:10] ,end='\n')
        if (NumC==NumA):
            win=win+1
            print ("恭喜成功")
        else:
            loss=loss+1
            print ("加油加油")
        for i in range(10):
            boardA[i]="*"
            boardC[i]="*"
        print ()
    print("總共成功: "+ str(win))
    print("總共失敗: "+ str(loss))
MagicBall(1000)