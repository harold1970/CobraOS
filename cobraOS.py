#!/usr/local/bin/python3
        # Import smtplib for the actual sending function
import http
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
# Import the email modules we'll need
import webbrowser
import random


version = "4.0"
#gets edited with clear_Array,see_array and array
array1 = []
passwords = ["1971","2022"]
print("_____________________CobraOS",version,"_______________________")
print("please input user name")
user_name = input()

print("hello",user_name)

while True:

    command = input("please input command:")
    
    if(command == "+"):
        print("first number")
        math1 = float(input())
        
        print("second number")
        math2 = float(input())
        
        print(math1 + math2)
  
    if(command == "/"):
        print("first number")
        math1 = float(input())
        
        print("second number")
        math2 = float(input())
        
        print(math1 / math2)

    if(command == "*"):
        print("first number")
        math1 = float(input())
        
        print("second number")
        math2 = float(input())
        
        print(math1 * math2)

    if(command == "-"):
        print("first number")
        math1 = float(input())
        
        print("second number")
        math2 = float(input())
        
        print(math1 - math2)

        
            
    
    #shutdown the OS
    if(command == "shutdown"):
        print("exiting...")
        exit()

    
    #shows the first 100 digits of pi
    if(command == "pi_100"):
        print("3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679")
   
    #add something to the array
    if(command == "array"):
        array1.append(input("add something:"))
  
    #see the array
    if(command == "see_array"):
        print(array1)
  
    #view all commands
    if(command == "help"):
        print("help: view all commands")
        
        print("shutdown: shutdown OS")
        #the math operaters
        print("*: multiply two numbers")
        print("-: subtract two numbers")
        print("+: add two numbers")
        print("/: divide two numbers")
        

        print("pi_100: view the first 100 digits of pi")
        print("see_array: view the list")
        print("array: add something to the list")
        print("clear_array: clears the array")
        print("version: see the version of the OS")
        print("admin: allows admin control")
        print("passwords: see passwords and or add passwords")
        print("logout: leaves admin account but does not shutdown the OS")    
        print("browser: opens a website(in dev), www.docs.com, www.doc_viewer.com")
    #empty the array
    if(command == "clear_array"):
        array1.clear()

    #views the version of the OS
    if(command == "version"):
        print("version",version)
        
        lastcommand = "CobraOS"

    
    #random number 0,100
    if(command == "random"):
        high = int(input("how high do you want it to go?:"))
        dice = random.randint(0,high)
        print(dice)
        
        lastcommand = "random"

    if(command == "admin"):
        adminpass = input("please input the password:")
        if adminpass in passwords:
            print("correct!")
            admin = True

   
    if(command == "passwords"):
        if(admin == True):
            print(passwords)
            print("do you want to add a password for accsessing the admin powers?")
            YN = input("y or n:")
            if(YN == "y"):
                passwords.append(input("add a password:"))
        else:
            print("you need admin control")
    
    if(command == "logout"):
        YN = input("y or n:")
        if(YN == "y"):
            admin = False 
        else:
            print("you are not logged in to admin")
    

    
    if(command == "browser"):
        www = input("please input a web address:")
        if(www == "www.docs.com"):
            
            dname = input("name:")
            body = input()
            docs = [dname,body]
            print("continue browsing?")
            YN = input("y/n:")
            if(YN == "y"):
                www = input("please input a web address:")
            else:
                pass      
        if(www == "www.doc_viewer.com"):
            print(docs)
            if(YN == "y"):
                www = input("please input a web address:")
            else:
                pass
    