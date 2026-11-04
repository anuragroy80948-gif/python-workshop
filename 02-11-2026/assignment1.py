# area of circle,square,triangle,rectangle using while and ladder if
import sys
while True:
    print("press0 for exit")
    print("press1 for area of circle")
    print("press2 for area of triangle")
    print("press3 for area of square")
    print("press4 for area of rectangle")

    ch = int(input("Enter your choice: "))
    if(ch==0):
            sys.exit("thank you!!")
    
    if (ch==1):
          value = float(input("Enter the radius "))
          result=value*value*22/7
          print("area of circle is ",result)


    if (ch==2):
          base = float(input("Enter the value of base"))
          height = float(input("Enter the value of height"))
          result=base*height*1/3
          print("area of triangle is ",result)


    if (ch==3):
          value = float(input("Enter the value of side "))
          result=value*value
          print("area of square is ",result)

    if (ch==4):
          length = float(input("Enter the value of length "))
          len = float(input("Enter the value of breadth "))
          result=length*len
          print("area of rectangle is ",result)    