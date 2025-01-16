import os
import shutil
import time
from datetime import datetime
now = datetime.now()
timedate = now.strftime("%d/%m/%Y %H:%M:%S")
approved = False
transac = False
main = True
upbal = 0.0
nbal = 0.0
vertical = '\u2551'
horizontal = '\u2550'
top_left = '\u2554'
top_right = '\u2557'
bottom_left = '\u255a'
bottom_right = '\u255d'


def header():
    width, _ = shutil.get_terminal_size()
    print(f"{horizontal * (120)}")
    print("                                   █████╗ ████████╗███╗   ███╗   ███╗   ███╗ ██████╗ ")
    print("                                  ██╔══██╗╚══██╔══╝████╗ ████║   ████╗ ████║██╔═══██╗")
    print("                                  ███████║   ██║   ██╔████╔██║   ██╔████╔██║██║   ██║")
    print("                                  ██╔══██║   ██║   ██║╚██╔╝██║   ██║╚██╔╝██║██║   ██║")
    print("                                  ██║  ██║   ██║   ██║ ╚═╝ ██║██╗██║ ╚═╝ ██║╚██████╔╝")
    print("                 ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝ ".center(width, " "))

def registr():
    loop = True

    while loop:
        os.system('cls')
        width, _ = shutil.get_terminal_size()
        print(f"{horizontal * (120)}")
        print(f"{vertical}{'        REGISTRATION       '}{vertical}".center(width, "="))
        print(f"{horizontal * (120)}")
        print("")
        while True:
            name = input(space+"Enter your Name: ")
            strnm = name.replace(" ", "")
            if not strnm.isalpha():
                print(space+"         Invalid Input!")
            else:
                break
        while True:
            try:
                pin = int(input(space+"Enter your Pin: "))
                break
            except:
                print(space+"-----------Invalid Input-----------")
        while True:
            try:
                amount = int(input(space+"Enter Amount: "))
                break
            except:
                print(space+"-----------Invalid Input-----------")
        pins = str(pin)
        amounts = str(amount)
        namel = name.lower()
        loop1 = True
        try:
            file = open("C:/customers/" + namel + ".txt", "x")
            file.write(name)
            file.write("\n")
            file.write(pins)
            file.write("\n")
            file.write(amounts)
            file.close()
            while loop1:
                l = str(input(space+"Y to confirm,N to cancel(y/n): "))
                l = l.lower()
                try:
                    if l == 'y':
                        loop = False
                        print("")
                        print(f"{vertical}{'    REGISTRATION SUCCESS   '}{vertical}".center(width, "^"))
                        print("")
                        nameup = name.capitalize()
                        print(space+"Account:..................... "+ nameup)
                        print(space + "Balance:....................₱" , amount)
                        break

                    elif l == 'n':
                        os.remove("C:/customers/" + namel + ".txt")
                        os.system('cls')
                        loop = False
                        loop1 = False
                        break
                except:
                    print(space+"-----------Invalid Input-----------")

        except:
            loop1 = True
            while loop1:
                print(space+"..........Name Already Taken!..........")
                l = input(space+"          Try again?(y/n): ")
                l = l.lower()
                try:
                    if l == 'y':
                        loop1 = False
                        os.system('cls')
                        continue
                    elif l == 'n':
                        loop1 = False
                        loop = False
                        break
                    else:
                        print(space + "-----------Invalid Input-----------")
                        continue
                except:
                    print(space + "-----------Invalid Input-----------")
                    continue


def withd():
    lo = False
    loop = True
    nw = False
    nn = True
    witt = False
    transac = False
    os.system("cls")
    while loop:
        os.system("cls")
        width, _ = shutil.get_terminal_size()
        print(f"{horizontal * (120)}")
        print(f"{vertical}{'          WITHDRAW         '}{vertical}".center(width, "="))
        print(f"{horizontal * (120)}")
        pas = False
        while nn:
            print("")
            name = input(space + "Enter your Name: ")
            namel = name.lower()
            try:
                file = open("C:/customers/" + namel + ".txt", "x")
                file.close()
                loop1 = True
                nw = True
                while loop1:
                    print(space + ".......Entered Name does not exist.......")
                    l = input(space + "          Try again?(y/n): ")
                    l = l.lower()
                    try:
                        if nw:
                            os.remove("C:/customers/" + namel + ".txt")
                            nw = False
                        if l == 'y':
                            loop1 = False
                            pas = False
                            continue
                        elif l == 'n':
                            loop = False
                            nn = False
                            break
                        else:
                            print(space + "1-----------Invalid Input-----------")
                            continue
                    except:
                        print(space + "21-----------Invalid Input-----------")
                        continue
            except:
                pas = True
                break
        while pas:
            try:
                print(space + "Enter your Pin: ", end="")
                pin = int(input(""))
                file = open("C:/customers/" + namel + ".txt", "r")
                file1 = file.readlines()
                file2 = file1[1]
                file2 = int(file2)
                file.close()
                if pin == file2:
                    approved = True
                    witt = True
                    loop = False

                    break
                else:
                    loop1 = True
                    while loop1:
                        print(space + "-----------Incorrect Pin-----------")
                        l = input(space + "  Do you want to try again?y/n: ")

                        l = l.lower()
                        try:
                            if l == 'y':
                                loop1 = False
                                continue
                            elif l == 'n':
                                loop = False
                                pas = False
                                break
                            else:
                                print(space + "3-----------Invalid Input-----------")
                                continue
                        except:
                            print(space + "4-----------Invalid Input-----------")
                            continue
            except:
                print(space + "5-----------Invalid Input-----------")
                continue


        while witt:
            while True:
                try:
                    am = float(input(space + "Amount to Withdraw: "))
                    break
                except:
                    print(space + "6-----------Invalid Input-----------")
                    continue
            bal = open("C:/customers/" + namel + ".txt", "r")
            bal1 = bal.readlines()
            bal2 = bal1[2]
            bal2 = float(bal2)
            file.close()
            if am > bal2:
                loop1 = True
                while loop1:
                    print(space + "       Insufficient Balance!       ")
                    l = input(space + "         Try again? y/n?: ")
                    l = l.lower()
                    try:
                        if l == 'y':
                            loop1 = False
                            continue
                        elif l == 'n':
                            witt = False
                            break
                    except:
                        print(space + "7-----------Invalid Input-----------")
                        continue
            elif am <= bal2:
                loop1 = True
                while loop1:
                    try:
                        print("")
                        print(space, "₱" , am, "Confirm Amount(y) or Cancel(n): ", end="")
                        l = input("")
                        l = l.lower()

                        if l == 'y':
                            witt = False
                            upbal = bal2 - am
                            upbal = int(upbal)
                            upbal2 = str(upbal)
                            file.close()
                            upbal3 = (upbal2 + "\n")
                            with open("C:/customers/" + namel + ".txt", 'r', encoding='utf-8') as file:
                                data = file.readlines()

                            data[2] = upbal3

                            with open("C:/customers/" + namel + ".txt", 'w', encoding='utf-8') as file:
                                file.writelines(data)

                            transac = True
                            lo = True
                            break

                        elif l == 'n':
                            loop = False
                            witt = False
                            loop1 = False
                            break
                    except:
                        print(space + "8-----------Invalid Input-----------")
                        continue
            else:
                print(space + "9-----------Invalid Input-----------")
                os.system('cls')
    while lo:
        nameup = name.capitalize()
        spacetime = ("Date & Time: ")
        spacename = ("Account Name: ")
        spacewith = ("Withdrew Amount ")
        spacebalance = ("Remaining Balance: ")
        am2 = str(am)
        upbal0 = str(upbal)
        f = open("C:/Receipt/receipt.txt", "a")
        f.write(spacetime + timedate)
        f.write("\n")
        f.write(spacename + nameup)
        f.write("\n")
        f.write(spacewith + am2)
        f.write("\n")
        f.write(spacebalance + upbal0)
        f.write("\n")
        f.close()
        t = input(space + "Do you want receipt? (y/n): ")
        t = t.lower()
        if t == 'y':
            if transac:
                width, _ = shutil.get_terminal_size()
                print("")
                print(f"{vertical}{'          RECEIPT          '}{vertical}".center(width, "^"))

                print(space + "Account:....................." + nameup)
                print(space + "Balance:....................₱", upbal)
                print(space + "Withdrew Amount:.............₱", am)
                print("")
                lo = False
                break
        elif t == 'n':
            break
        else:
            print(space + "10-----------Invalid Input-----------")
            continue




def depot():
    lo = False
    res = False
    loop = True
    balance = False
    neym = True
    nw = False
    while loop:
        os.system("cls")
        width, _ = shutil.get_terminal_size()
        print(f"{horizontal * (120)}")
        print(f"{vertical}{'           DEPOSIT         '}{vertical}".center(width, "="))
        print(f"{horizontal * (120)}")
        print("")
        pas = True
        pas1 = False
        while neym:
            name = input(space+"Enter your Name: ")
            namel = name.lower()
            try:
                file = open("C:/customers/" + namel + ".txt", "x")
                file.close()
                loop1 = True
                nw = True
                while loop1:
                    print(space + ".......Entered Name does not exist.......")
                    l = input(space + "          Try again?(y/n): ")
                    l = l.lower()
                    try:
                        if nw:
                            os.remove("C:/customers/" + namel + ".txt")
                            nw = False
                        if l == 'y':
                            loop1 = False
                            pas = False
                            continue
                        elif l == 'n':
                            loop = False
                            neym = False
                            pas = False
                            break
                        else:
                            print(space + "-----------Invalid Input-----------")
                            continue
                    except:
                        print(space + "-----------Invalid Input-----------")
                        continue
            except:
                pas = True
                break
        while pas:
            try:
                pin1 = str(input(space + "Enter your Pin: "))
                pin = int(pin1)
                file = open("C:/customers/" + namel + ".txt", "r")
                file1 = file.readlines()
                file2 = file1[1]
                file2 = int(file2)
                file.close()
                if pin == file2:
                    approved = True
                    loop = False
                    balance = True
                    break
                else:
                    loop1 = True
                    print(space + "-----------Incorrect Pin-----------")
                    while loop1:
                        l = input(space + "  Do you want to try again?y/n: ")
                        l = l.lower()
                        try:
                          if l == 'y':
                            loop1 = False
                            continue
                          elif l == 'n':
                            loop = False
                            loop1 = False
                            pas = False
                            balance = False
                            break
                          else:
                            print(space + "-----------Invalid Input-----------")
                            continue
                        except:
                            print(space + "-----------Invalid Input-----------")
                            continue
            except:
                print(space + "-----------Invalid Input-----------")
                continue

        while balance:
            ask = False
            try:
                nbal = int(input(space + "Enter Balance: "))
                ask = True
            except:
                print(space + "-----------Invalid Input-----------")
                continue
            while ask:
                print(space+ "₱", nbal, "Confirm Amount(y) or Cancel(n): ", end="")
                l = input()
                l = l.lower()

                try:
                    if l == 'y':
                        balance = False
                        break
                    elif l == 'n':
                        ask = False
                        balance = False
                        loop = False
                        pas = False
                        continue
                except:
                    print(space + "-----------Invalid Input-----------")
                    continue
        if pas:
            bal = open("C:/customers/" + namel + ".txt", "r")
            bal1 = bal.readlines()
            bal2 = bal1[2]
            bal2 = float(bal2)
            upbal = bal2 + nbal
            upbal = int(upbal)
            upbal2 = str(upbal)
            upbal3 = (upbal2)
            file.close()
            with open("C:/customers/" + namel + ".txt", 'r', encoding='utf-8') as file:
                data = file.readlines()

            data[2] = upbal3

            with open("C:/customers/" + namel + ".txt", 'w', encoding='utf-8') as file:
                file.writelines(data)

            transac = True
            res = True
            lo = True
    while lo:
        nameup = name.capitalize()
        spacetime = ("Date & Time: ")
        spacename = ("Account Name: ")
        spacewith = ("Deposit Amount ")
        spacebalance = ("Updated Balance: ")
        am2 = str(nbal)
        upbal0 = str(upbal)
        f = open("C:/Receipt/receipt.txt", "a")
        f.write(spacetime + timedate)
        f.write("\n")
        f.write(spacename + nameup)
        f.write("\n")
        f.write(spacewith + am2)
        f.write("\n")
        f.write(spacebalance + upbal0)
        f.write("\n")
        f.close()
        t = input(space + "Do you want receipt? (y/n): ")
        t = t.lower()
        if t == 'y':
            if res:
                width, _ = shutil.get_terminal_size()
                print("")
                print(f"{vertical}{'          RECEIPT          '}{vertical}".center(width, "^"))

                print(space + "Account:....................." + nameup)
                print(space + "Balance:.....................₱", upbal)
                print(space + "Deposit Amount:..............₱", nbal)
                print("")
                lo = False
                break
        elif t == 'n':
            break
        else:
            print(space + "-----------Invalid Input-----------")
            continue


def checkb():
    loop = True
    bloop = True
    nw = False
    approved = False
    os.system("cls")
    while loop:
        os.system("cls")
        width, _ = shutil.get_terminal_size()
        print(f"{horizontal * (120)}")
        print(f"{vertical}{'        CHECK BALANCE      '}{vertical}".center(width, "="))
        print(f"{horizontal * (120)}")
        pas = False
        while bloop:
            print("")
            name = input(space + "Enter your Name: ")
            namel = name.lower()
            try:
                file = open("C:/customers/" + namel + ".txt", "x")
                file.close()
                loop1 = True
                nw = True
                while loop1:
                    l = ""
                    print(space + ".......Entered Name does not exist.......")
                    l = input(space + "          Try again?(y/n): ")
                    l = l.lower()
                    try:
                        if nw:
                            os.remove("C:/customers/" + namel + ".txt")
                            nw = False
                        if l == 'y':
                            loop1 = False
                            pas = False
                            continue
                        elif l == 'n':
                            loop = False
                            bloop = False
                            break
                        else:
                            print(space + "-----------Invalid Input-----------")
                            continue
                    except:
                        print(space + "-----------Invalid Input-----------")
                        continue
            except:
                pas = True
                break
        while pas:
            try:
                pin = int(input(space + "Enter your Pin: "))
                file = open("C:/customers/" + namel + ".txt", "r")
                file1 = file.readlines()
                file2 = file1[1]
                file2 = int(file2)
                file.close()
                if pin == file2:
                    approved = True
                    loop = False
                    break
                else:
                    loop1 = True
                    print(space + "-----------Incorrect Pin-----------")
                    while loop1:

                        l = input(space + "  Do you want to try again?y/n: ")
                        l = l.lower()
                        try:
                            if l == 'y':
                                loop1 = False
                                continue
                            elif l == 'n':
                                loop = False
                                pas = False
                                break
                            else:
                                print(space + "-----------Invalid Input-----------")
                                continue
                        except:
                            print(space + "-----------Invalid Input-----------")
                            continue
            except:
                print(space + "-----------Invalid Input-----------")
                continue

        if approved:
            bal = open("C:/customers/" + namel + ".txt", "r")
            bal1 = bal.readlines()
            bal2 = bal1[2]
            width, _ = shutil.get_terminal_size()
            print("")
            print(f"{vertical}{'          BALANCE          '}{vertical}".center(width, "^"))
            nameup = name.capitalize()
            print(space + "Account:....................." + nameup)
            print(space + "Balance:.....................₱", bal2)
            print("")


def sendm():
    loop = True
    bloop = True
    nw = False
    rec = False
    transac = False
    sendA = False
    lo = False

    os.system("cls")
    while loop:
        os.system("cls")
        width, _ = shutil.get_terminal_size()
        print(f"{horizontal * (120)}")
        print(f"{vertical}{'      TRANSFER MONEY       '}{vertical}".center(width, "="))
        print(f"{horizontal * (120)}")
        pas = False
        while bloop:
            print("")
            name = input(space + "Enter your Name: ")
            namel = name.lower()
            try:
                file = open("C:/customers/" + namel + ".txt", "x")
                file.close()
                loop1 = True
                nw = True
                while loop1:
                    l = ""
                    print(space + ".......Entered Name does not exist.......")
                    l = input(space + "          Try again?(y/n): ")
                    l = l.lower()
                    try:
                        if nw:
                            os.remove("C:/customers/" + namel + ".txt")
                            nw = False
                        if l == 'y':
                            loop1 = False
                            pas = False
                            continue
                        elif l == 'n':
                            loop = False
                            bloop = False
                            break
                        else:
                            print(space + "-----------Invalid Input-----------")
                            continue
                    except:
                        print(space + "-----------Invalid Input-----------")
                        continue
            except:
                pas = True
                break
        while pas:
            try:
                print(space + "Enter your Pin: ", end="")
                pin = int(input(""))
                file = open("C:/customers/" + namel + ".txt", "r")
                file1 = file.readlines()
                file2 = file1[1]
                file2 = int(file2)
                file.close()
                if pin == file2:
                    approved = True
                    loop = False
                    rec = True
                    break
                else:
                    loop1 = True
                    print(space + "-----------Incorrect Pin-----------")
                    while loop1:
                        l = input(space + "  Do you want to try again?y/n: ")

                        l = l.lower()
                        try:
                            if l == 'y':
                                loop1 = False
                                continue
                            elif l == 'n':
                                loop = False
                                pas = False
                                rec = False
                                break
                            else:
                                print(space + "-----------Invalid Input-----------")
                                continue
                        except:
                            print(space + "-----------Invalid Input-----------")
                            continue
            except:
                print(space + "-----------Invalid Input-----------")
                continue


    while rec:
        name = input(space + "Name of the Recipient: ")
        name2 = name.lower()
        try:
            file = open("C:/customers/" + name2 + ".txt", "x")
            file.close()
            loop1 = True
            nw = True
            while loop1:
                print(space + ".......Entered Name does not exist.......")
                l = input(space + "          Try again?(y/n): ")
                l = l.lower()
                try:
                    if nw :
                        os.remove("C:/customers/" + name2 + ".txt")
                        nw = False
                    if l == 'y':
                        loop1 = False
                        pas = False
                        sendA = True
                        continue
                    elif l == 'n':
                        loop = False
                        rec = False
                        sendA = False
                        break
                    else:
                        print(space + "-----------Invalid Input-----------")
                        continue
                except:
                    print(space + "-----------Invalid Input-----------")
                    continue
        except:
            if namel != name2:
                sendA = True
                break
            else:
                print(space + "-----------Invalid Input-----------")
                continue
    while sendA:
        while True:
            try:
                am = float(input(space + "Amount to Send: "))
                break
            except:
                print(space + "-----------Invalid Input-----------")
                continue
        bal = open("C:/customers/" + namel + ".txt", "r")
        bal1 = bal.readlines()
        bal2 = bal1[2]
        bal2 = float(bal2)
        file.close()
        if am > bal2:
            loop1 = True
            while loop1:
                print(space + "       Insufficient Balance!       ")
                l = input(space + "         Try again? y/n?: ")
                l = l.lower()
                try:
                    if l == 'y':
                        loop1 = False
                        continue
                    elif l == 'n':
                        sendA = False
                        loop1 = False
                        break
                except:
                    print(space + "-----------Invalid Input-----------")
                    continue
        elif am <= bal2:
            loop1 = True
            while loop1:
                try:
                  print(space + "₱", am, "Confirm Amount(y) or Cancel(n): ", end="")
                  l = input()
                  l = l.lower()

                  if l == 'y':
                        upbal = bal2 - am
                        upbal = int(upbal)
                        upbal2 = str(upbal)
                        upbal3 = (upbal2 + "\n")
                        with open("C:/customers/" + namel + ".txt", 'r', encoding='utf-8') as file1:
                            data1 = file1.readlines()

                        upbal4 = str(upbal3)
                        data1[2] = upbal4

                        with open("C:/customers/" + namel + ".txt", 'w', encoding='utf-8') as file1:
                            file1.writelines(data1)
                        balr = open("C:/customers/" + name2 + ".txt", "r")
                        balr1 = balr.readlines()
                        balr4 = balr1[2]
                        balr4 = float(balr4)
                        upbalr = balr4 + am
                        upbalr = int(upbalr)
                        upbalr2 = str(upbalr)
                        upbalr3 = (upbalr2)
                        balr.close()
                        with open("C:/customers/" + name2 + ".txt", 'r', encoding='utf-8') as file:
                            data = file.readlines()

                        data[2] = upbalr3

                        with open("C:/customers/" + name2 + ".txt", 'w', encoding='utf-8') as file:
                            file.writelines(data)

                        transac = True
                        loop1 = False
                        sendA = False
                        lo = True

                  elif l == 'n':
                        loop1 = False
                        sendA = False
                        continue
                except:
                  print(space + "-----------Invalid Input-----------")
                  continue
        else:
            print(space + "-----------Invalid Input-----------")

    while lo:
        nameup = namel.capitalize()
        nameup1 = name2.capitalize()
        spacetime = ("Date & Time: ")
        spacesname = ("Sender Account: ")
        spacername = ("Recipient Account: ")
        spacewith = ("Recieved Amount: ")
        spacebalance = ("Updated Balance(Sender): ")
        am2 = str(am)
        upbal0 = str(upbal)
        upbal01 = str(upbalr)
        f = open("C:/Receipt/receipt.txt", "a")
        f.write(spacetime + timedate)
        f.write("\n")
        f.write(spacesname + nameup)
        f.write("\n")
        f.write(spacebalance + upbal0)
        f.write("\n")
        f.write(spacername + nameup1)
        f.write("\n")
        f.write(spacewith + am2)
        f.write("\n")
        f.close()
        t = input(space + "Do you want receipt? (y/n): ")
        t = t.lower()
        if t == 'y':
            if transac:
                width, _ = shutil.get_terminal_size()
                print("")
                print(f"{vertical}{'          RECEIPT          '}{vertical}".center(width, "^"))
                print(space + "Sender Account:.............." + nameup)
                print(space + "Balance:.....................₱", upbal)
                print("")
                print(space + "Recipient Account:...........", nameup1)
                print(space + "Balance:.....................₱", upbalr)
                print("")
                lo = False
                break
        elif t == 'n':
            break
        else:
            print(space + "-----------Invalid Input-----------")
            continue
def changp():
    loop = True
    bloop = True
    nw = False
    rec = False
    transac = False
    sendA = False
    lo = False
    approved = False
    os.system("cls")
    while loop:
        os.system("cls")
        width, _ = shutil.get_terminal_size()
        print(f"{horizontal * (120)}")
        print(f"{vertical}{'        CHANGE PIN         '}{vertical}".center(width, "="))
        print(f"{horizontal * (120)}")
        pas = False
        while bloop:
            print("")
            name = input(space + "Enter your Name: ")
            namel = name.lower()
            try:
                file = open("C:/customers/" + namel + ".txt", "x")
                file.close()
                loop1 = True
                nw = True
                while loop1:
                    l = ""
                    print(space + ".......Entered Name does not exist.......")
                    l = input(space + "          Try again?(y/n): ")
                    l = l.lower()
                    try:
                        if nw:
                            os.remove("C:/customers/" + namel + ".txt")
                            nw = False
                        if l == 'y':
                            loop1 = False
                            pas = False
                            continue
                        elif l == 'n':
                            loop = False
                            bloop = False
                            break
                        else:
                            print(space + "-----------Invalid Input-----------")
                            continue
                    except:
                        print(space + "-----------Invalid Input-----------")
                        continue
            except:
                pas = True
                break
        while pas:
            try:
                print(space + "Enter your Pin: ", end="")
                pin = int(input(""))
                file = open("C:/customers/" + namel + ".txt", "r")
                file1 = file.readlines()
                file2 = file1[1]
                file2 = int(file2)
                file.close()
                if pin == file2:
                    approved = True
                    loop = False
                    rec = True
                    break
                else:
                    loop1 = True
                    print(space + "-----------Incorrect Pin-----------")
                    while loop1:
                        l = input(space + "  Do you want to try again?y/n: ")

                        l = l.lower()
                        try:
                            if l == 'y':
                                loop1 = False
                                continue
                            elif l == 'n':
                                loop = False
                                pas = False
                                rec = False
                                break
                            else:
                                print(space + "-----------Invalid Input-----------")
                                continue
                        except:
                            print(space + "-----------Invalid Input-----------")
                            continue
            except:
                print(space + "-----------Invalid Input-----------")
                continue
    while rec:
        no = False
        loop1 = True
        while approved:
            try:
                while loop1:
                    print(space + "Enter new Pin: ", end="")
                    chpin = int(input(""))
                    l = str(input(space + "Y to Confirm,N to Cancel (y/n): "))
                    l = l.lower()
                    try:
                        if l == 'y':
                            approved = False
                            loop1 = False
                            no = True
                            break
                        elif l == 'n':
                            loop1 = False
                            approved = False
                            rec = False
                            no = False
                            break
                    except:
                        print(space + "-----------Invalid Input-----------")
                        continue
            except:
                print(space + "-----------Invalid Input-----------")
                continue
        if no:
            upbal2 = str(chpin)
            upbal3 = str(upbal2 + "\n")
            with open("C:/customers/" + namel + ".txt", 'r', encoding='utf-8') as file:
                data = file.readlines()

            data[1] = upbal3

            with open("C:/customers/" + namel + ".txt", 'w', encoding='utf-8') as file:
                file.writelines(data)

            print(f"{vertical}{'    CHANGE PIN SUCCESS!    '}{vertical}".center(width, "^"))
            break


while main:
    loop1 = False
    space = '\t\t\t\t\t'
    header()
    width, _ = shutil.get_terminal_size()
    print(f"\t\t\t\t\t{top_left}{horizontal * (33)}{top_right}")
    print(f"\t\t\t\t\t{vertical}{'    [1] Register {No account?    '}{vertical}")
    print(f"\t\t\t\t\t{vertical}{'    [2] Withdraw                 '}{vertical}")
    print(f"\t\t\t\t\t{vertical}{'    [3] Deposit                  '}{vertical}")
    print(f"\t\t\t\t\t{vertical}{'    [4] Transer Money            '}{vertical}")
    print(f"\t\t\t\t\t{vertical}{'    [5] Check Balance            '}{vertical}")
    print(f"\t\t\t\t\t{vertical}{'    [6] Change Pin               '}{vertical}")
    print(f"\t\t\t\t\t{vertical}{'    [0] Exit                     '}{vertical}")
    print(f"\t\t\t\t\t{bottom_left}{horizontal * (33)}{bottom_right}")
    try:
        cho = int(input(space+"Enter Choice: "))
        os.system('cls')
        print("")
        if cho == 1:
            registr()
            loop1 = True
        elif cho == 2:
            withd()
            loop1 = True
        elif cho == 3:
            depot()
            loop1 = True
        elif cho == 4:
            sendm()
            loop1 = True
        elif cho == 5:
            checkb()
            loop1 = True
        elif cho == 6:
            changp()
            loop1 = True
        elif cho == 0:
            main = False
            break
        else:
            print(space + "-----------Invalid Input-----------")
            loop1 = True
            os.system('cls')
    except ValueError:
        print(space + "22-----------Invalid Input-----------")
        loop1 = True
    while loop1:
        l = input(space+"Do you want another Transaction? y/n?")
        l = l.lower()
        try:
            if l == 'y':
                loop1 = False
                os.system('cls')
                continue
            elif l == 'n':
                main = False
                os.system('cls')
                break
            else:
                print(space + "-----------Invalid Input-----------")
                continue
        except:
            print(space + "-----------Invalid Input-----------")
            time.sleep(3)
            continue

space = '\t\t\t\t\t'
width, _ = shutil.get_terminal_size()
print(f"{horizontal * (120)}")
print(f"{vertical}{'      THANK YOU FOR USING ATM.MO!       '}{vertical}".center(width, "="))
print(f"{horizontal * (120)}")
os.system("PAUSE")








