import os
import sys
import math
import time
from os import system, name  

def clear(): 
    if name == 'nt': 
        _ = system('cls')   
    else: 
        _ = system('clear') 

def sockMerchant(ar):
    duplicatesRemoved = set(ar)
    totalPairs = 0
    for num in duplicatesRemoved:
        numCount = ar.count(num)
        pairsInCount = math.floor(numCount/2)
        totalPairs+=pairsInCount
    return(totalPairs)

print(r"""


          ,-----.         
          %%%%%%%         
          #######         
          %%%%%%%         
          |     |         
          |     |         
          |     |         
          (     `-.       
           `.      `.     
             `.      `.   
               `-.     \  
                  `-.___) 


Challenge: Sock Merchant

ASCII Artist: Krogg @ http://sock.ascii.u   k/
      
  """)

time.sleep(5)
clear() 
time.sleep(2)

ar = list(map(int, input("Input the list of numbers that represent the sock colors: \n").rstrip().split()))

result = sockMerchant(ar)

print("\nYou can match " + str(result) + " pairs of socks.\n")