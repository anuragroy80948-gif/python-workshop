#percentage 
per=int(input("enter your percentage"))
if(per>=60):
    print("I Div.")
elif(per>=45 and per<60):
    print("II Div.")
elif(per>=33 and per<45):
    print("III Div.")
else:
    print("Fail")