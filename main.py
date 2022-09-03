import webbrowser
# import random                                                 replaced random with secrets for better security and to avoid seed misuse
import secrets
import sys
import string
import os
import time
import storage
import pyperclip
#replacing random() with secrets()
def menu():
    os.system('cls')
    print("\nHomepage\n 1) Random 10 digit password (recommended)\n 2) Generate Password of Custom Length\n 3) Show Saved Passwords\n 4) Edit Saved Password\n 5) DELETE ALL SAVED PASSWORDS!! \n")
    print("Press 0 to Exit ")
def saving(pm):
    
    
    dec = input("Do you want to save this password? \nPress 'Y' to save or any other key to go back to menu: ")
    if dec == 'Y' or dec == 'y':
        storage.writeF(pm)
        print("Saving password")
        loading(0.05)
        os.system('cls')
        print("\nCopied to clipboard\n")
        pyperclip.copy(pm)
        print("Saved Successfully!\n Access Saved Passwords from Homepage\n")
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
    l1 = secrets.choice(string.ascii_uppercase)
    l2 = secrets.choice(string.ascii_lowercase)
    l3 = secrets.choice(string.ascii_lowercase)
    l8 = secrets.choice(string.ascii_lowercase)
    l10 = secrets.choice(string.ascii_lowercase)
    l6 = secrets.choice(string.punctuation)
    l4 = str(secrets.choice(string.digits))
    l7 = str(secrets.choice(string.digits))
    l5 = secrets.choice(string.punctuation)
    l9 = secrets.choice(string.punctuation)
    result = l1 + l2 + l3 + l8 + l10 + l6 + l4 + l7 + l5 + l9
    print("Your 10 digit secure password is " + result)
    return result


def customPass():
    os.system('cls')
    s1 = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    while True:
        try:
            plen = int(input("Enter length of password: "))
            break
        except ValueError or OverflowError:
            print("BAD INPUT")
            time.sleep(1)
            os.system('cls')
    # s = []
    # print(s)
    # result = "".join(secrets.choices(s, k=plen))
    result = ''.join(secrets.choice(s1) for i in range(plen))
    print("Your Randomly Generated Password: ", end="")
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
            loading(0.05)
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
        print("Thanks for using Poppy. Exiting")
        loading(0.01)
        os.system('cls')
        exit()
    elif cho == 3:
        def main():
            got = storage.readF()
            if got == 1:
                while True:
                    try:
                        back = int(input("NOTE: THIS IS READ ONLY.\nPress 0 to Home: "))
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
        os.system('cls')
        print("Opening file in editing mode\n WARNING: ONLY CHANGE IF YOU KNOW WHAT YOU'RE DOING! ", end="")
        loading(0.1)
        webbrowser.open("pass.txt")
        time.sleep(1)
        startPage()
        
    elif cho == 5:
        storage.delF()
        startPage()
        
    else:
        os.system('cls')
        print(
            "Option not found.\nThis option '"+ str(cho) + "' is either unavailable or under construction in this service, please contact admin for more info")
        loading(0.05)
        startPage()

startPage()
