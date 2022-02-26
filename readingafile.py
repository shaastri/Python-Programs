myfirstfile=open("readingcontentlinebyline.txt","r")

print()

print("Is my file able to read?",myfirstfile.readable())

firstlineoffile=myfirstfile.readline()

print(firstlineoffile,end="")

secondlineoffile=myfirstfile.readline()

print(secondlineoffile,end="")

thirdlineoffile=myfirstfile.readline()

print(thirdlineoffile,end="")

fourthlineoffile=myfirstfile.readline()

print(fourthlineoffile,end="")

fifthlineoffile=myfirstfile.readline()

print(fifthlineoffile,end="")




myfirstfile.close()

print()
print("Is my file is closed or Not?",myfirstfile.closed)

