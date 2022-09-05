#!/usr/local/bin/python3


from lib2to3.pgen2.token import PERCENT
import math
import os
import random
from datetime import datetime
from multiprocessing import cpu_count
from multiprocessing.dummy import Array
from operator import truediv

benchmark = 100
version = "4.2"
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
        
        
        print("new_array: creates a new array")
        print("edit_new+: add something to the array")
        print("edit_new-: removes something from the new array")
        print("view_array_new: views the array")
        print("derp_dog: does math to see how derpy your dog is")
        print("next_update: see the next update")

    #empty the array
    if(command == "clear_array"):
        array1.clear()

    #views the version of the OS
    if(command == "version"):
        print("version",version)
        
        

    
    #random number 0,100
    if(command == "random"):
        high = int(input("how high do you want it to go?:"))
        dice = random.randint(0,high)
        print(dice)
        
        

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
    
    if(command == "cpu"):
        print(cpu_count())  
    
    if(command == "new_array"):
        if(admin == True):
            name = input("name your array:")
            
            print("your new array is called:",name)
            name = []
        
    if(command == "edit_new+"):
        if(admin == True):   
            name.append(input("add something:"))
        
    
    if(command == "edit_new-"):
        if(admin == True): 
            delete = input("please input the name of the item you want to remove:")
            name.remove(delete)

    if(command == "view_array_new"):
        if(command == True):    
            print(name)
    
    if(command == "next_update"):
        print("the next update will allow you to email people and you can check you inbox")
    

    if(command == "derp_dog"):
        dog_name = input("please input dogs name:")
        if(dog_name == "Stella","stella"):
            print("you now have admin control.")
            admin = True
            stupidity = int(input("how high is the chance that yor dog will be distracted by the TV(0-20):"))
            zoomies = int(input("please input your dog's frequency of zoomies(0-20):"))
            happyness = int(input("please input your dog's happyness when they see you(0-20):"))
            fly = int(input("how high of a chance that you dog will chase a fly(0-20)"))
            clumsyness = int(input("how clumsy is your dog (0-20):"))
            print("_|_",dog_name, "derpyness_|_")
            print("\|/___________________\|/")
            print("%",stupidity + zoomies + happyness + fly + clumsyness,"derp")
        else:   
            stupidity = int(input("how high is the chance that yor dog will be distracted by the TV(1-20):"))
            zoomies = int(input("please input your dog's frequency of zoomies(1-20):"))
            happyness = int(input("please input your dog's happyness when they see you(1-20):"))
            fly = int(input("how high of a chance that you dog will chase a fly(1-20)"))
            clumsyness = int(input("how clumsy is your dog (1-20):"))
            print("_|_",dog_name, "derpyness_|_")
            print("\|/___________________\|/")
            print("%",stupidity + zoomies + happyness + fly + clumsyness,"derp")
        