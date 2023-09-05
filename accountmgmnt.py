from accounts import AD
import os
import datetime



x = datetime.datetime.now()
print(x.strftime("%c"))



class accmgmnt :
   def createaccount(e):
     with open("accountholders.txt","a") as fp:
       fp.write(str(e))
       fp.write("\n")

   def main() :
    ch= 0
    while(ch!=10):
     print("*******************************Welcome***********************************")  
     print("--------------------select operation------------------")
     print("1-Show Balance ")  
     print("2-Deposite  ")  
     print("3-Withdraw ")  
     print("4-Transfer")  
     print("5-Account statement ")  
     print("6-Exit")

     
     ch=input("Enter the choice you want : ")
     if ch == '1':
       id=int(input("Enter id : "))
       accmgmnt.showbalance(id)
     elif ch =='2':
       id=int(input("Enter id : "))
       accmgmnt.depositmoney(id)
     elif ch == '3':
       id=int(input("Enter id : "))
       accmgmnt.withdraw(id)
     elif ch == '4':
       id1=int(input("Enter Your account id : "))
       id2=int(input("Enter the Beneficiary id : "))
       accmgmnt.withdraw(id1)
       accmgmnt.Transfer(id1,id2)
     elif ch == '5':
       id1=int(input("Enter Your account id : "))
       accmgmnt.showaccountstatement(id1)
     elif ch == '6':
       exit()
     else :
       print("-------ERROR ! Enter Correct Choice---------")

 

   def showbalance(id):
    x = datetime.datetime.now()
    if(os.path.exists("accountholders.txt")):
            with open("accountholders.txt","r") as fp:
                allacc = []
                for accounts in fp:
                    try:
                        accounts.index(str(id),0,4)
                    except:
                        pass
                    else:
                        accounts = accounts.split(",") 
                        ans = input("Do you want to see account balance(y/n)?")
                        if(ans.lower() == 'y'): 
                           print("Your Account Balance is : ",float(accounts[2]))
                           print("Current Time is : ",x)
                          
      

   def login():
     x = datetime.datetime.now()
     id=int(input("Enter the id :"))
     pwd=input("Enter Password : ")
     if(os.path.exists("accountholders.txt")):
            with open("accountholders.txt","r") as fp:
              for accounts in fp:
                if (str(id) in accounts) and (str(pwd) in accounts):
                  print("Login Succesfull")
                  accmgmnt.main()
                else:
                    print("")

   def depositmoney(id):
       x = datetime.datetime.now()
       if(os.path.exists("accountholders.txt")):
            with open("accountholders.txt","r") as fp:
                allacc = []
                found = False
                for accounts in fp:
                    try:
                        accounts.index(str(id),0,4)
                    except:
                        pass
                    else:
                        found = True 
                        accounts = accounts.split(",")  
                        accounts[2]= float(accounts[2])
                        Am = float(input("Enter amount : "))
                        accounts[2]=accounts[2] + Am
                        accounts[2] = str(accounts[2])
                        accounts = ",".join(accounts)
                    finally:
                        allacc.append(accounts)
                            
            if(found):
                with open("accountholders.txt","w") as fp:
                    for accounts in allacc:
                        fp.write(accounts)
            else:
                print("Record not found")
       else:
            print("File is not present")
       

   def withdraw(id1):
       x = datetime.datetime.now()      
       if(os.path.exists("accountholders.txt")):
            with open("accountholders.txt","r") as fp:
                allacc = []
                found = False
                for accounts in fp:
                    try:
                        accounts.index(str(id1),0,4)
                    except:
                        pass
                    else:
                        found = True 
                        accounts = accounts.split(",") 
                        accounts[2]= float(accounts[2])
                        Am = float(input("Enter amount : "))
                        accounts[2]=accounts[2]-Am
                        accounts[2] = str(accounts[2])
                        accounts = ",".join(accounts)
                    finally:
                        allacc.append(accounts)
                            
          
            if(found):
                with open("accountholders.txt","w") as fp:
                    for accounts in allacc:
                        fp.write(accounts)
            else:
                print("Record not found")
       else:
            print("File is not present")

   def Transfer(id1,id2):
     x = datetime.datetime.now()
     y= print("Current Time is : ", x.strftime("%c"))
     if(os.path.exists("accountholders.txt")):
            with open("accountholders.txt","r") as fp:
                allacc = []
                found = False
                for accounts in fp:
                    try:
                        accounts.index(str(id2),0,4)
                    except:
                        pass
                    else:
                        found = True 
                        accounts = accounts.split(",")  
                        accounts[2]= float(accounts[2])
                        Am = float(input("Confirm amount : "))
                        accounts[2]=accounts[2] + Am
                        print("Amount Transferred Successfully")
                        accounts[2] = str(accounts[2])
                        accounts = ",".join(accounts)
                        with open("transfer.txt","a") as fp:
                            details = str(id1)+","+str(id2)+","+str(Am)+","+ x.strftime("%c")+"\n"
                            fp.write(details)
                    finally:
                        allacc.append(accounts)
                                      
            if(found):
                with open("accountholders.txt","w") as fp:
                    for accounts in allacc:
                        fp.write(accounts)
            else:
                print("Record not found")
     else:
            print("File is not present")

   def showaccountstatement(id):
     x = datetime.datetime.now()
     if(os.path.exists("transfer.txt")):
            with open("transfer.txt","r") as fp:
                allacc = []
                for accounts in fp:
                    try:
                        accounts.index(str(id),0,4)
                    except:
                        pass
                    else:
                        accounts = accounts.split(",")
                        ans = input("Do you want to see account balance(y/n)?")
                        if(ans.lower() == 'y'): 
                           print("-------------------------------------------------------------")
                           print("Transferred from Account id :",accounts[0])
                           print("Transfer To Account id :",accounts[1])
                           print("Transfer Amount : ",accounts[2])
                           print("Transfer Time :",accounts[3])
                           print("Current Time is : ",x)
                           print("-------------------------------------------------------------")
                          
      
   
     