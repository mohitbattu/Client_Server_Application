"""
Test.py file is used to test all the five
functionalities present in the file server1.py.Here
we have created five different types of test cases and used these
created modules of file operations to create, write, read and has
Moved the current working directory for the current user to the specified folder
which resides in the current folder.
"""
import unittest
import fileopn

class Test_FileOpt(unittest.TestCase):
    """
    Here we have taken five various types of test cases to test
    the server code present in the fileserver.py file.where the server in turn
    establishes a connection between the client file.However all the five
    test cases were ran successfully and had used the four different file operations
    which are present in the fileopn.py file.
    """
    def test1(self):
        """
        This is the first test case where the userid is mohii07.Folder with the name of lion
        is created with the help of create_folder() function, file is written with the help of
        wfile() function and then a file has been read with the help of a rfile() function.
        We have changed the path of folder by using the fucntion called as path_ch().
        Here the name of the file is sounds with a message content written in it as
        "Lion roars when it is hungry".
        """
        opera = fileopn.FilOpt("mohii07")

        createfol = opera.create_folder("lion")
        self.assertEqual(createfol, True)

        writefil = opera.wfile("lion", "sounds", "Lion roars when it is hungry")
        self.assertEqual(writefil, True)

        readfil = opera.rfile("lion", "sounds")
        self.assertEqual(readfil, "Lion roars when it is hungry")

        change = opera.path_ch("lion")
        self.assertEqual(change, True)

    def test2(self):
        """
        In the second test case,the userid is ramesh07.Folder with the name of cars
        is created with the help of create_folder() function, file is written with the help of
        wfile() function
        and then a file has been read with the help of a rfile() function.We have changed
        the path of folder by using the fucntion called as path_ch().Here the name of the file is
        Lambo with a message content written in it as "lambhorgini is a top auto gear car".
        """
        opera = fileopn.FilOpt("ramesh07")

        createfol = opera.create_folder("cars")
        self.assertEqual(createfol, True)

        writefil = opera.wfile("cars", "Lambo", "lambhorgini is a top auto gear car")
        self.assertEqual(writefil, True)

        readfil = opera.rfile("cars", "lambo")
        self.assertEqual(readfil, "lambhorgini is a top auto gear car")

        change = opera.path_ch("cars")
        self.assertEqual(change, True)

    def test3(self):
        """
        In the third test case,the userid is sita07.Folder with the name of flowers
        is created with the help of create_folder() function, file is written with the help of
        wfile() function
        and then a file has been read with the help of a rfile() function.We have changed
        the path of folder by using the fucntion called as path_ch().Here the name of the file is
        rose with a message content written in it as "sita likes rose flower".
        """
        opera = fileopn.FilOpt("sita07")

        createfol = opera.create_folder("flowers")
        self.assertEqual(createfol, True)

        writefil = opera.wfile("flowers", "rose", "sita likes rose flower")
        self.assertEqual(writefil, True)

        readfil = opera.rfile("flowers", "rose")
        self.assertEqual(readfil, "sita likes rose flower")

        change = opera.path_ch("flowers")
        self.assertEqual(change, True)

    def test4(self):
        """
        In the fourth test case,the userid is durga07.Folder with the name of football
        is created with the help of create_folder() function, file is written with the help of
        wfile() function
        and then a file has been read with the help of a rfile() function.We have changed
        the path of folder by using the fucntion called as path_ch().Here the name of the file is
        player with a message content written in it as "durga's favourite player is messi".
        """
        opera = fileopn.FilOpt("durga07")

        createfol = opera.create_folder("football")
        self.assertEqual(createfol, True)

        writefil = opera.wfile("football", "player", "durga's favourite player is messi")
        self.assertEqual(writefil, True)

        readfil = opera.rfile("football", "player")
        self.assertEqual(readfil, "durga's favourite player is messi")

        change = opera.path_ch("football")
        self.assertEqual(change, True)

    def test5(self):
        """
        In the fifth test case,the userid is jitisha07.Folder with the name of chef
        is created with the help of create_folder() function, file is written with the help of
        wfile() function
        and then a file has been read with the help of a rfile() function.We have changed
        the path of folder by using the fucntion called as path_ch().Here the name of the file is
        cook with a message content written in it as "jitisha loves to cook".
        """
        opera = fileopn.FilOpt("jitisha07")

        createfol = opera.create_folder("chef")
        self.assertEqual(createfol, True)

        writefil = opera.wfile("chef", "cook", "jitisha loves to cook")
        self.assertEqual(writefil, True)

        readfil = opera.rfile("chef", "cook")
        self.assertEqual(readfil, "jitisha loves to cook")

        change = opera.path_ch("chef")
        self.assertEqual(change, True)

if __name__ == "__main__":
    unittest.main()
