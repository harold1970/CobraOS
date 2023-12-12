
import os
import random
import sys
from multiprocessing import cpu_count

version = "1.4.3"

print("_____________________CobraOS",version,"_______________________")
print("please input user name")
global user_name
user_name = input()



# print(f"Comm")
class Command:
    def __init__(self, commands):
        if self.name in commands:
            raise RuntimeError("That command name is already used.")
        commands[self.name] = self

    @property
    def name(self):
        raise NotImplemented

    def call(self, *args):
        raise NotImplemented
    
    def get_input(self):
        return ()

class BinaryOperator(Command):
    def get_input(self):
        l = float(input("left: "))
        r = float(input("right: "))
        return l, r

class Add(BinaryOperator):
    name = "+"
    def call(self, left, right):
        #return left + right
        print(left + right)

class Subtract(BinaryOperator):
    name = "-"
    def call(self, left, right):
        #return left - right
        print(left - right)

class Divide(BinaryOperator):
    name = "/"
    def call(self, left, right):
        print(left / right)

class Multiply(BinaryOperator):
    name = "*"
    def call(self, left, right):
        print(left * right)

class Shutdown(Command):
    name = "shutdown"
    def call(self):
        print("exiting...")
        exit()

class Pi_100(Command):
    name = "pi_100"
    def call(self):
        print("3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679")

class Help(Command):
    name = "help"
    def call(self):
        for x in commands:
            print(f"--> {x}")

class Version(Command):
    name = "version"
    def call(self): 
        print(f"version{version}")

class Dice(Command):
    name = "random"
    def get_input(self):
        max = int(input("how high do you want it to go?:"))
        
        return (max,)
    def call(self, max):
        dice = random.randint(0,max)
        print(dice)    

class Cpu(Command):
    name = "cpu"
    def call(self):
        print(cpu_count())

class Derp_Dog(Command):
    name = "derp_dog"
    def call(self):
        dog_name = input("please input dogs name:")
        if(dog_name == "Stella","stella"):
            print("you now have admin control.")
            admin = True
            stupidity = int(input("how high is the chance that yor dog will be distracted by the TV(0-20):"))
            zoomies = int(input("please input your dog's frequency of zoomies(0-20):"))
            happyness = int(input("please input your dog's happyness when they see you(0-20):"))
            fly = int(input("how high of a chance that you dog will chase a fly(0-20)"))
            clumsyness = int(input("how clumsy is your dog (0-20):"))
            print(dog_name, "derpyness")
            print("↓___________________↓")
            print("%",stupidity + zoomies + happyness + fly + clumsyness,"derp")
            dog_name = "(:"
        else:   
            stupidity = int(input("how high is the chance that yor dog will be distracted by the TV(1-20):"))
            zoomies = int(input("please input your dog's frequency of zoomies(1-20):"))
            happyness = int(input("please input your dog's happyness when they see you(1-20):"))
            fly = int(input("how high of a chance that you dog will chase a fly(1-20)"))
            clumsyness = int(input("how clumsy is your dog (1-20):"))
            print(dog_name, "derpyness")
            print("↓___________________↓")
            print("%",stupidity + zoomies + happyness + fly + clumsyness,"derp")

class Cls(Command):
    name = "cls"
    def call(self):
        os.system('cls')   

class Ping(Command):
    name = "ping"
    def call(self):
        hostname = str(input())
        response = os.system("ping " + hostname)

        #and then check the response...
        if response == 0:
            print(hostname, 'is up!')
        else:
            print(hostname, 'is down!')

class UserName(Command):
    name = "username"
    def call(self):
        print(user_name)

class User_Edit(Command):
    name = "user_edit"
    def call(self):
        
        print("do you want to change the username")
        YN = input("y or n:")
        if(YN == "y"):
            user_name = str(input("input new username →"))

class Restart(Command):
    name = "restart"
    def call(self):
        os. system('cls') 
        os.execv(sys.executable, ['python'] + sys.argv)       


#a=(1,2)
# b=[1,2]
# a[0] == b[0] # True
# a[0] = 3 # Exception: tuples are immutable
# b[0] = 3 # OK: arrays are mutable
#where the commands go
commands = {}
Add(commands)
Subtract(commands)
Divide(commands)
Multiply(commands)
Shutdown(commands)
Help(commands)
Pi_100(commands)
Version(commands)
Dice(commands)
Cpu(commands)
Derp_Dog(commands)
Cls(commands)
Ping(commands)
UserName(commands)
User_Edit(commands)
Restart(commands)









while True:
    command = input(f"{user_name}/cobraOS|--> ")
    command = command.strip()
    if(command == ""):
        continue
    if command not in commands:
        print("command not found")
        continue

    instance = commands[command]
    args = instance.get_input()
    instance.call(*args) # .call(args[0], args[1])
    

