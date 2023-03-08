# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
name = input ("input your name: ")
studentId = input ("input your student id: ")
print("My name is "+name+" and my student id is "+studentId)
"""

""""
import random
times = 0
guess = 0
ans = random.randint(1,100)

print("The guess number is between 1 to 100. ")
for times in range(6):
    guess = int (input ("Input the guess number: "))
    
    if guess == ans:
        break
    
    if guess < ans:
        print ("Your guess is too Low.")

    if guess > ans:
        print ("Your guess is too high.")
        
if guess == ans:
    times=str(times+1)
    print ("Congratulations, you guessed number in " +times + " guesses!")
if guess != ans:
    ans= str(ans)
    print  ("Oh no! You don't guess. The answer is "+ans)
"""

import random
times = 0
guess = 0
tmp=str(random.randint(1,9))

ans=[]
guess=[]

A=0
B=0
ans.append(tmp)  

tmp=str(random.randint(1,9))
while (tmp==ans[0]):
    tmp=str(random.randint(1,9))
ans.append(tmp) 
    
tmp=str(random.randint(1,9))
while (tmp==ans[0] or tmp==ans[1]):
    tmp=str(random.randint(1,9))
ans.append(tmp) 
    
tmp=str(random.randint(1,9))
while (tmp==ans[0] or tmp==ans[1] or tmp==ans[2]):
    tmp=str(random.randint(1,9))
ans.append(tmp)   


for times in range(5):
    guess = str(input ("Guess? "))
    if guess[0] == ans[0] and guess[1] == ans[1] and guess[2] == ans[2] and guess[3] == ans[3]:
        A=4
        break
    else:
        print("Guess wrong!")
        A=0
        B=0
        for i in range(4):
            for j in range (4):
                if ans[i]==guess[j]:
                    if i==j:
                        A=A+1
                    else:
                        B=B+1
        print( str(A)+ "A " +str(B) + "B")

if A == 4:
    times=str(times+1)
    print ("Congratulations, you guessed  in " +times + " times!")
else:
    ans= str(ans)
    print  ("Oh no! You loss. The answer is "+"".join(ans))
        

