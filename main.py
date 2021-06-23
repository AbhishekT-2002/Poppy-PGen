import webbrowser
import random
import sys
import string
import os
import time
import storage

def menu():
    print(" Main Menu\n 1) Random 10 digit password [best for daily and regular uses]\n 2) Generate password of custom length\n 3) See your saved passwords list\n 4) Delete saved password file\n 5) Edit Password file\n")
    print("press 0 to exit the program")
def saving(pm):
    dec = input("Do you want to save this password so you can access it later? \n Press 'Y' to save or any other key to go back to menu: ")
    if dec == 'Y' or dec == 'y':
        storage.writeF(pm)
        print("Saving password")
        loading(0.05)
        os.system('cls')
        print("Password successfully saved in file!\n Access the password list from main menu\n ")
        print("Returning to menu")
        loading(0.05)
    else:
        print("Returning to menu")
        loading(0.02)
        os.system('cls')
        menu()


def loading(t):
    loads = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    for char in loads:
        time.sleep(t)
        sys.stdout.write(char)
def randPass():
    os.system('cls')
    UcaseList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
    LcaseList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    NumList = [1, 2, 3, 4, 5, 6, 7, 4, 8, 9, 0]
    SymList = ["@", "$", "%", "&", "!", "?", ]
    Mathlist = ["+", "*", "-", "/"]
    l1 = random.choice(UcaseList)
    l2 = random.choice(LcaseList)
    l3 = random.choice(LcaseList)
    l8 = random.choice(LcaseList)
    l10 = random.choice(LcaseList)
    l6 = random.choice(Mathlist)
    l4 = str(random.choice(NumList))
    l7 = str(random.choice(NumList))
    l5 = random.choice(SymList)
    l9 = random.choice(SymList)
    result = l1 + l2 + l3 + l8 + l10 + l6 + l4 + l7 + l5 + l9
    print("Your 10 digit secure password is " + result)
    return result


def customPass():
    os.system('cls')
    s1 = string.ascii_uppercase
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    while True:
        try:
            plen = int(input("Enter length of password: "))
            break
        except ValueError or OverflowError:
            print("BAD INPUT")
            time.sleep(1)
            os.system('cls')
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)
    result = "".join(random.choices(s, k=plen))
    print("Your randomly generated password: ", end="")
    print(result)
    return result


def startPage():
    os.system('cls')
    menu()
    while True:
        try:
            cho = int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('cls')
            print( "ERROR")
            print("ONLY INTEGERS ARE ALLOWED!!\n RESTART PROGRAM OR CONTACT ADMIN IF PROBLEM PERSISTS.")
        menu()
    if cho == 1:
        r = randPass()
        saving(r)
        startPage()
    elif cho == 2:
        r = customPass()
        saving(r)
        startPage()
    elif cho == 0:
        os.system('cls')
        print("Thanks for using my program. exiting ")
        loading(0.1)
        os.system('cls')
        exit()
    elif cho == 3:
        def main():
            got = storage.readF()
            if got == 1:
                while True:
                    try:
                        back = int(input("NOTE: THIS IS READ ONLY.\nPress 0 to go back to main menu: "))
                        break
                    except ValueError:
                        os.system('cls')
                        print("BAD INPUT!!")
                        time.sleep(0.5)
                        main()
                if back == 0:
                    os.system('cls')
                    startPage()
                else:
                    os.system('cls')
                    print("BAD INPUT!!")
                    time.sleep(0.5)
                    storage.readF()
                    main()
            else:
                startPage()
        main()
    elif cho == 4:
        storage.delF()
        startPage()
    elif cho == 5:
        os.system('cls')
        print("Opening file in editing mode\n WARNING: ONLY CHANGE IF YOU KNOW WHAT YOU'RE DOING! ", end="")
        loading(0.5)
        webbrowser.open("pass.txt")
        time.sleep(1)
        startPage()
        
    else:
        os.system('cls')
        print(
            "Option not found.\nThis option '"+ str(cho) + "' is either unavailable or under construction in this service, please contact admin for more info")

startPage()
