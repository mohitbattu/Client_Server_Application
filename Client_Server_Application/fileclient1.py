"""The fileclient1 file is the subset of the fileclient file
where it collects the name of the user,userid and password.
such that it helps the user to get registered in the name of
register folder.
"""
async def creg(reader, writer):
    """This function takes the two inputs called as
    reader and writer from the user.Its main purpose is to
    setup a user account by collecting the details such as
    username,userid and password.
    """
    ride = await reader.read(100)
    gsm = ride.decode().strip()
    # Name of the user is collected given by the user
    namme = input(gsm)
    writer.write(namme.encode())
    ride = await reader.read(100)
    gsm = ride.decode().strip()
    # Here the userid is collected given by the user.
    uid = input(gsm)
    writer.write(uid.encode())
    dim = await reader.read(100)
    msg = dim.decode().strip()
    # Here password is created by the user.
    pas = input(msg)
    writer.write(pas.encode())
    det = await reader.read(100)
    msg = det.decode().strip()
    print(msg)
    print("----Now you can Login----")
