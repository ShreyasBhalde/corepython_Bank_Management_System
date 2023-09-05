from accountmgmnt import accmgmnt
from accounts import AD
import random
import datetime
import os




S=0
while S!=10:
 print("******************WELCOME TO BANK APPLICATION******************")
 print("-------------------------select Sevice----------------------")
 print("1-Create Account ")  
 print("2-Login ")

 S=input("Which Service You want : ")  
 if S=="1" :
  nm=input("Enter Name : ")
  bal=input("Enter Account opening Amount : ")
  id=input("Enter an Id : ")
  pwd=input("Enter Password : ")
  e=AD(nm,bal,id,pwd)
  accmgmnt.createaccount(e)
 elif S=="2":
   
   accmgmnt.login()
 else:
   print("Enter Correct Value")


        



    

 