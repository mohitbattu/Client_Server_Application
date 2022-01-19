"""This programming file is used as a backend
side where it collects all the inputs from
client and sends the information requested by the user.
"""
import asyncio
import signal
from fileserver1 import login
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def register(reader, writer):
    """It is used for creating and registering
    an account with password, username and name If the details
    are already present in the working directory then
    it displays message as Request Denied or you are already registered.
    If the entered details are not present then it registers the account
    with the user entered details.The entered details are then checked
    whether it is present or not in the current working directory.
    """
    mgs = "Enter your name :"
    writer.write(mgs.encode())
    div = await reader.read(100)
    name = div.decode().strip()
    mih = "Create a User Name : "
    writer.write(mih.encode())
    daop = await reader.read(100)
    usid = daop.decode().strip()
    man = "Enter your Password :"
    writer.write(man.encode())
    deng = await reader.read(100)
    password = deng.decode().strip()
    check = False
    # Details entered by the usr are checked here
    pth = "C:\\Users\\raobk\\Desktop\\Assignment_3\\root\\admin\\Registration.txt"
    with open(pth, 'r') as read:
        for line in read:
            if usid in line:
                if password in line:
                    check = True
                    break
    # If the entered details are not present then acc is registered.
    if not check:
        with open(pth, 'a') as wriite:
            wriite.write(usid + ':')
            wriite.write(password + ', \n')
        mpk = "User Registered Succcessfully."
        writer.write(mpk.encode())
    # If the details are already present
    # in the working directory then it displays message as
    # Request Denied or you are already registered
    else:
        lpm = "Request Denied\nYou are already Registered"
        writer.write(lpm.encode())



async def choose(reader, writer):
    """Gives an option for user to login and register his account.
    if the user has prompted to register then that specific function
    would be called such that user will enter his basic details.
    else it will call a login function where the user will
    enter his userid and password to login his account."""
    message = """Choice Register or Login
    1. Register
    2. Login
    Enter your choice :"""
    writer.write(message.encode())
    dum = await reader.read(100)
    choose = dum.decode().strip()
    if choose == '1':
        await register(reader, writer)
    else:
        await login(reader, writer)

async def main():
    """Here server is initiated at 127.0.0.1 at
    the port number of 8888.This is the main function where it
    retrieves the information given by the user at the client side
    and produces a result with respect to the information given by
    the user thus establishing a connection between the client and server."""
    server = await asyncio.start_server(
        choose, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
