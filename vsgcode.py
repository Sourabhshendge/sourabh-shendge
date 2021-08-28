import math

print("calculate area of shape ")
print("")
print("1.area of rectangle")
print("2.area of pentagon")
print("3.area of hexagon")
print("4.area of trapazium")
print("5.area of circle")
print("6.area of oval")
print("7.area of triangle")
x=int(input("enter your choice : "))

if(x==1):
    l=int(input("enter length : "))
    b=int(input("enter breath : "))
    a=l*b
    print("area is = ",a)


elif(x==2):
    s=int(input("enter side"))
    a=1.72048*s*s
    print("area is = ",a)


elif(x==3):
    x=float(input("enter length"))
    a=(3*math.sqrt(3)*math.pow(x,2))/2.0
    print("area is = ",a)
    

elif(x==4):
    h=int(input("height : "))
    b1=int(input("base 1 : "))
    b2=int(input("base 2 : "))
    a=((b1+b2)/2)*h
    print("area is = ",a)

elif(x==5):
    r=int(input("radius : "))
    a=(22/7)*r*r
    print("area is = ",a)


elif(x==6):
    r1=int(input("radius : "))
    r2=int(input("radius : "))
    a=(22/7)*r1*r2
    print("area is = ",a)

elif(x==7):
    h=int(input("height : "))
    b=int(input("base : "))
    a=0.5*h*b
    print("area is = ",a)

else:
    print("wrong choice!")





