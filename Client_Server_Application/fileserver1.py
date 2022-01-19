""" This file is a subset of fileserver programming file,where
it contains a module of login functionalities.When user logins with his account details,
then it provides user to access some basic file operations such as
read, write and create.
"""
import fileinput
from fileopn import FilOpt

async def login(reader, writer):
    """This function is used for entering
    the login details where user will type his
    UserID and Password such that  user gets access
    to perform basic file operations like read,
    write and create."""
    mlkp = """\t\tLogin Form
    Enter UserID   : """
    writer.write(mlkp.encode())
    dpio = await reader.read(100)
    usid = dpio.decode().strip()
    mpsk = "    Enter Password : "
    writer.write(mpsk.encode())
    dodp = await reader.read(100)
    passw = dodp.decode().strip()
    filph = "C:\\Users\\raobk\\Desktop\\Assignment_3\\root\\admin\\Registration.txt"
    confirm = 0
    boww = True
    # If the user has already logined in a server
    # then resultant message is shown as Access Denied.
    with open(filph, 'r') as pamu:
        for line in pamu:
            if usid in line:
                if passw in line:
                    confirm = 1
                    if "logged" in line:
                        msh = "You have logged in already\nAccess Denied"
                        writer.write(msh.encode())
                        boww = False
                        break

    if boww:
        for line in fileinput.FileInput(filph, inplace=1):
            if usid in line:
                if passw in line:
                    line = line.rstrip()
                    line = line.replace(line, line + "logged\n")
            print(line, end='')
    if confirm != 1:
        # if there are incorrect details then it will display as invalid
        # username or password.
        meow = "Invalid Username or Password"
        writer.write(meow.encode())
    elif confirm == 1 and boww:
        try:
            msg = """
            Login Access Granted.\nWelcome\nCommand are:
            1.Folder Creation
            2.File Writing
            3.File Reading
            4.List of Folders
            5.Change Path
            0.LogOut"""
            writer.write(msg.encode())
            user = FilOpt(usid)
            while True:
                dot = await reader.read(100)
                medop = dot.decode().strip()
                if medop == '1':
                    # Used for creating the folder
                    msh = "Enter folder name : "
                    writer.write(msh.encode())
                    dplo = await reader.read(100)
                    fname = dplo.decode().strip()
                    conv = user.create_folder(fname)
                    if conv:
                        msk = "Folder Created!"
                        writer.write(msk.encode())
                    else:
                        mplp = "Folder Exists"
                        writer.write(mplp.encode())
                elif medop == '2':
                    # Used for writing the contents in the file.
                    mskl = "Enter folder name : "
                    writer.write(mskl.encode())
                    dplp = await reader.read(50)
                    folname = dplp.decode().strip()
                    mlpl = "Enter file name : "
                    writer.write(mlpl.encode())
                    damm = await reader.read(50)
                    filename = damm.decode().strip()
                    mghjk = "Enter the d : "
                    writer.write(mghjk.encode())
                    dimo = await reader.read(50)
                    ilom = dimo.decode().strip()
                    hoe = user.wfile(folname, filename, ilom)
                    if hoe:
                        mklo = "File Created"
                        writer.write(mklo.encode())
                elif medop == '3':
                    # Used for reading the contents in the file.
                    mtr = "Enter folder name : "
                    writer.write(mtr.encode())
                    dck = await reader.read(100)
                    folname = dck.decode().strip()
                    mcd = "Enter file name : "
                    writer.write(mcd.encode())
                    dng = await reader.read(100)
                    filename = dng.decode().strip()
                    kng = str(user.rfile(folname, filename))
                    writer.write(kng.encode())
                elif medop == '4':
                    # Used for displaying the number of files present in the
                    # folder.
                    lname, lsize, lcr, lmod = user.lis_of()
                    muu = "Name      Size         Created           Modified"
                    writer.write(muu.encode())
                    doi = await reader.read(1000)
                    mow = doi.decode().strip()
                    sname = str(" ".join(lname))
                    writer.write(sname.encode())
                    dos = await reader.read(1000)
                    mat = dos.decode().strip()
                    ssize = str(" ".join(map(str, lsize)))
                    writer.write(ssize.encode())
                    duc = await reader.read(1000)
                    msg = duc.decode().strip()
                    scr = str("  ".join(map(str, lcr)))
                    writer.write(scr.encode())
                    djt = await reader.read(1000)
                    msg = djt.decode().strip()
                    smod = str("  ".join(map(str, lmod)))
                    writer.write(smod.encode())
                    dinc = await reader.read(1000)
                    mbbs = dinc.decode().strip()
                elif medop == '5':
                    # It is used for changing the folder name.
                    mgs = "Enter Folder name : "
                    writer .write(mgs.encode())
                    ddat = await reader.read(100)
                    oname = ddat.decode().strip()
                    nar = user.path_ch(oname)
                    if nar:
                        messi = "Changed Successfully"
                    else:
                        messi = "NOT Exists"
                    writer.write(messi.encode())

                elif medop == '0':
                    # Used for logging out of the session.
                    break
        except Exception as e:
            print(e)
        finally:
            for line in fileinput.FileInput(filph, inplace=1):
                if usid in line:
                    if passw in line:
                        line = line.rstrip()
                        line = line.replace(line, f"{usid}:{passw},\n")
                print(line, end='')
            mmauw = "Log Out Successfull"
            writer.write(mmauw.encode())