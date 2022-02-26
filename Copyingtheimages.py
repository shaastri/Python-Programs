file_object_for_image1=open("F:\\Python-3.10.0\\File Handling in Python\\Capture.PNG","rb")

file_object_for_image2=open("F:\\Python-3.10.0\\File Handling in Python\\Newimage.PNG","wb")

bytes=file_object_for_image1.read()

file_object_for_image2.write(bytes)

print("New image is copied successfully with the name of Newimage.PNG")
