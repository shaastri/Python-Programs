import os,sys

filename=input("Enter the file name that you want to check:")

if os.path.isfile(filename):
    print("Yes the file name you entered is existing",filename)
    filename=open(filename,"r")

else:
    print("No the file name that you are entered is not exist",filename)
    sys.exit(0)

Contentinthefileexist=filename.read()
print(Contentinthefileexist)

