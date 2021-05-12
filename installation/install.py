

import os, errno


# Function to write a file at a given path
def WriteFileInPath(content, path):
    try:
        with open(path, "w+") as f:
            f.write(content)  # TODO: CHECK IF NEW LINE CHARACTER IS NEEDED OR NOT
            f.close()
            return "Created " + path
    except IOError as e:
        print(e)
        return False


# This function creates given folders.
def installFolder(folder):
    try:
        os.makedirs(folder)
        print("Created directory", folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


main =
# Start installing the files
print(
    "This project was made by Aekansh Dixit (First Year Student of PES University, Bengaluru) for the Python Project Assignments of the first semester.")
print("Creating directories...")
installFolder("Password Keeper")
installFolder("Password Keeper/bin")
installFolder("Password Keeper/res")
print("Creating main file...")
print(WriteFileInPath(main, "Password Keeper/main.py"))
print("Creating other files...")
print(WriteFileInPath(al, "Password Keeper/res/al.py"))
print(WriteFileInPath(ap, "Password Keeper/res/ap.py"))
print(WriteFileInPath(d, "Password Keeper/res/d.py"))
print(WriteFileInPath(f, "Password Keeper/res/f.py"))
print(WriteFileInPath(m, "Password Keeper/res/m.py"))
print(WriteFileInPath(s, "Password Keeper/res/s.py"))
print("Installation finished.")
