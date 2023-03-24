import os
import time
import sys
def writeF(p):
        wF = open("pass.txt", "a+")
        wF.write(p)
        os.system('cls')
        wF.write("\nDescription:- ")
        msg = input("\nEnter message/remarks/description for this password: ")
        wF.write(msg)
        wF.write("\n---------------------------------------------------------------\n")
def readF():
    if os.path.exists("pass.txt") == True:
        os.system('cls')
        rF = open("pass.txt", "r")
        print(rF.read())
        return 1
    else:
        os.system('cls')
        print("File not found")
        time.sleep(1)
        return 0
        
def delF():
    while True:
        try:
            conf = int(input("\nWARNING:THIS CHANGE IS PERMANENT\nPress 1 to confirm deletion / Any other key to cancel: "))
            # print("got integer")
            break
        except ValueError :
           exit()
    if conf == 1:
        if os.path.exists("pass.txt") == True:
            os.remove("pass.txt")
            os.system('cls')
            loading="XXXXXXXXXXXXX"
            for char in loading:
                sys.stdout.write(char)
                time.sleep(0.1)
            os.system('cls')
            print("Successfully Deleted")
            time.sleep(0.5)
        else:
            print("This file does not exist")
            time.sleep(1)          
    else:
        print("Operation cancelled")
        time.sleep(2)
