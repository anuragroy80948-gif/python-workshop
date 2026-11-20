#for create file
fp=open("myfile.text","w")
print(type(fp))
data=input("Enter data in a file ")
fp.write(data)
print("file created")
fp.close()