"""This programming file is used for performing basic file operations like
reading,writing and creating the file.With other functionalites like cf and lis
are used for changing the folder name, to represent the number of files in
folder.
"""

import os
import time


class FilOpt:
    """
    This class is used for creating, writing and reading.
    It is used for presenting a list of files in the current folder and
    also used to change the folder name.
    """
    def __init__(self, us):
        """Here we initialise all the variables that is going to be used in
        the later functions of the code.We also setup the path directory in the
        variable called as pthh.
        """
        # setting the folder path
        self.usn = us
        self.pthh = f"C:\\Users\\raobk\\Desktop\\Assignment_3\\root\\{self.usn}\\"
        self.oname = 0
        self.nname = 0
        self.crmn = 0
        self.mopl = 0
        self.bnlopk = 0
        self.fun = 0
        self.fns = 0
        self.fname = 0
        self.input = 0
        self.iuytr = 0
        self.fnpl = 0
        self.fname = 0
        self.data = 0
        self.foplk = 0
        self.super = 0
        self.coupen = 0
        self.mouno = 0
        self.pimm = 0
        self.pm = 0
        self.path = 0
        self.fol = 0
        try:
            os.makedirs(self.pthh)
        except Exception:
            pass

    def create_folder(self, name):
        """This function is used to create a
        folder with the name specified by the user.
        """
        # Here folder name is created and stored in the current working dir.
        self.mopl = name
        self.bnlopk = False
        self.fun = os.path.join(self.pthh, self.mopl)
        try:
            os.makedirs(self.fun)
            self.bnlopk = True
        # if a file exists then exception will be raised.
        except FileExistsError:
            print("File Exists")
        finally:
                return self.bnlopk

    def wfile(self, fname, name, inputd):
        """ The user enters some details which is written in the file.
        It provides a user to write the contents in the file.
        """
        # The function is used to write inside a file.
        self.fns = name
        self.fname = f"{fname}\\"
        self.input = inputd
        self.iuytr = False
        try:
            self.pm = os.path.join(self.pthh, self.fname)
            self.path = os.path.join(self.pm, self.fns)
            # print(self.path)
            with open(self.path, 'w') as iuy:
                iuy.write(self.input)
                self.iuytr = True
        except Exception as error:
            print(error)
        finally:
            return self.iuytr

    def rfile(self, fname, name):
        """Here it reads all the contents present in the file and
        then it prints the contents present in that file.
        """
        # This function is used to read a file contents.
        self.fnpl = name
        self.fname = f"{fname}\\"
        self.data = ''
        try:
            self.pimm = os.path.join(self.pthh, self.fname)
            self.path = os.path.join(self.pimm, self.fnpl)
            with open(self.path, 'r') as ride:
                self.data = ride.readlines()
        except Exception as error:
            return print(error)
        finally:
            return " ".join(self.data)

    def lis_of(self):
        """This function main priority is used to
        display the number of created folder
        in the working directory.
        """
        # Here it displays the number of files in the folder.
        self.foplk = os.listdir(self.pthh)
        self.super = []
        self.coupen = []
        self.mouno = []
        total_size = 0
        for flpl in self.foplk:
            self.fol = os.path.join(self.pthh, flpl)
            self.mouno.append(time.ctime(os.path.getmtime(f"{self.fol}")))
            self.coupen.append(time.ctime(os.path.getctime(f"{self.fol}")))
            for path, dirs, files in os.walk(self.fol):
                for fplm in files:
                    fpgh = os.path.join(path, fplm)
                    total_size += os.path.getsize(fpgh)
            self.super.append(total_size)
        return self.foplk, self.super, self.coupen, self.mouno

    def path_ch(self, oname):
        """It is used to mainly change the existing name of
        the folder.here the user is asked to enter the previous
        name of the folder and then it asks for a new name of the
        folder such that it will change the name of the current folder.
        """
        # Here it is used to change the name of the folder.
        self.oname = oname
        self.crmn = False

        try:
            os.chdir(self.pthh)
            self.crmn = True
        except Exception:
            pass
        finally:
            return self.crmn
