"""This programming file is used to take the inputs given by the user
which inturn establishes a connection with the server.Client file acts like a
front end to the user which displays all the functionalities to the user."""

import asyncio
import sys
from fileclient1 import creg

async def ClientProgram():
    """It collects the inputs from the user such as name of the folder,
    password, userid and username entered by the user.
     """
    rider, waiter = await asyncio.open_connection('127.0.0.1', 8888)
    choice = await rider.read(100)
    msg = choice.decode().strip()
    print(msg)
    choose = input()
    waiter.write(choose.encode())
    if choose == '1':
        # It is used for registering an account.
        await creg(rider,waiter)

    if choose != '1':
        # Here the user is logged in by entering his details.
        data = await rider.read(100)
        msg = data.decode().strip()
        # username is entered here.
        unam = input(msg)
        waiter.write(unam.encode())
        dut = await rider.read(100)
        mkh = dut.decode()
        # password is entered here.
        paas = input(mkh)
        waiter.write(paas.encode())
        din = await rider.read(10000)
        mgs = din.decode().strip()
        print(mgs)
        if mgs == "You have logged in already\nAccess Denied" or mgs == "Invalid Username or Password":
            sys.exit()
        while True:
            chice = input("Enter your choice : ")
            waiter.write(chice.encode())
            if chice == '1':
                # Here the folder is created.
                dot = await rider.read(100)
                mok = dot.decode().strip()
                fpn = input(mok)
                waiter.write(fpn.encode())
                dok = await rider.read(100)
                mpu = dok.decode().strip()
                print(mpu)
            elif chice == "2":
                # Here we can use it for writing the file.
                dit = await rider.read(50)
                mkh = dit.decode().strip()
                fman = input(mkh)
                waiter.write(fman.encode())
                doom = await rider.read(50)
                mon = doom.decode().strip()
                fpon = input(mon)
                waiter.write(fpon.encode())
                dpl = await rider.read(50)
                muno = dpl.decode().strip()
                # The contents typed by the user is collected here.
                dplo = input(muno)
                # The contents are then written into a file.
                waiter.write(dplo.encode())
                douy = await rider.read(100)
                msg = douy.decode().strip()
                print(msg)
            elif chice == "3":
                """Here the file contents are read and
                generates an output displaying the information
                present in the file."""
                dpt = await rider.read(100)
                mkh = dpt.decode().strip()
                # Folder name is taken here.
                fpom = input(mkh)
                waiter.write(fpom.encode())
                dpom = await rider.read(100)
                mnom = dpom.decode().strip()
                # file name is taken here.
                funn = input(mnom)
                waiter.write(funn.encode())
                dat = await rider.read(100)
                mopk = dat.decode().strip()
                print(mopk)
            elif chice == "4":
                """Here it will display the number of files
                present in the current working folder."""
                dokl = await rider.read(100)
                msgg = dokl.decode().strip()
                print(msgg)
                waiter.write("hi".encode())
                dutt = await rider.read(100)
                snpu = dutt.decode().strip()
                npp = list(snpu.split(" "))
                waiter.write("hello".encode())
                divn = await rider.read(200)
                soap = divn.decode().strip()
                sing = list(soap.split(" "))
                waiter.write("hello".encode())
                diet = await rider.read(900)
                srach = diet.decode().strip()
                creww = list(srach.split("  "))
                waiter.write("hello".encode())
                die = await rider.read(900)
                same = die.decode().strip()
                mod = list(same.split("  "))
                waiter.write("hello".encode())
                for fop in range(len(npp)):
                    # Here it will display the name, size, created and modified
                    # details of the file.
                    print(f"{npp[fop]}  {sing[fop]}  {creww[fop]}  {mod[fop]}")
            elif chice == '5':
                """Here it will change the path."""
                damp = await rider.read(100)
                munm = damp.decode().strip()
                # Current name of the folder is collected here.
                nmom = input(munm)
                waiter.write(nmom.encode())
                dirnm = await rider.read(100)
                mpgb = dirnm.decode().strip()
                print(mpgb)
            elif chice == "0":
                # Used to end the session.where the user logs out.
                break

        dklo = await rider.read(100)
        mplm = dklo.decode().strip()
        print(mplm)
    waiter.close()
asyncio.run(ClientProgram())
