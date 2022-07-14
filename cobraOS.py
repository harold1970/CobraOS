#/usr/local/bin/python3



import math
import random
version = "3.0"
#gets edited with clear_Array,see_array and array
array1 = []
passwords = ["1971","2022"]
print("_____________________CobraOS",version,"_______________________")
print("please input user name")
user_name = input()

print("hello",user_name)

while True:

    command = input("please input command:")
    #shutdown the OS
    if(command == "shutdown"):
        print("exiting...")
        exit()
    #Add two numbers
    if(command == "math"):
        print("this")
        math1 = float(input())
        print("plus this") 
        math2 = float(input())
        print("equal this")
        print(math1 + math2)
        
        lastcommand = "math"
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
        print("math: adds to numbers together")
        print("pi_100: view the first 100 digits of pi")
        print("see_array: view the list")
        print("array: add something to the list")
        print("clear_array: clears the array")
        print("version: see the version of the OS")
        print("admin: allows admin control")
        print("passwords: see passwords and or add passwords")
        print("logout: leaves admin account but does not shutdown the OS")    
    
    #empty the array
    if(command == "clear_array"):
        array1.clear()
        
        lastcommand = "clear_array"
    #views the version of the OS
    if(command == "CobraOS"):
        print("version",version)
        
        lastcommand = "CobraOS"
    #random number 0,100
    if(command == "random"):
        dice = random.randint(0,100)
        print(dice)
        
        lastcommand = "random"
    
    if(command == "admin"):
        adminpass = input("please input the password:")
        if adminpass in passwords:
            print("correct!")
            admin = True
        else:
            print("wrong password")
    
    if(command == "passwords"):
        if(admin == True):
            print(passwords)
            print("do you want to add a password for accsessing the admin powers?")
            YN = input("y or n:")
            if(YN == "y"):
                array1.append(input("add a password:"))
        else:
            print("you need admin control")
    
    if(command == "logout"):
        YN = input("y or n:")
        if(YN == "y"):
            admin = False 
        
        


    
