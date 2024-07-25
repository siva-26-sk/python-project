num1=int(input("enter the values:"))
values=[]
for i in range (1,num1+1):
    num2=int(input( ))
    values.append(num2)
    print("list=",num2)
"""a=int(input("values:"))
b=int(input("values:"))"""
print("entur ur operation:\n1.add\n2.sub\n3.div\n4.mul")
c=input("your choice(1,2,3,4):")
if(c=="1"):
    result=0
    for a in values:
        result=result+a
    print(result)
elif(c=="2"):
    result1=values[0]
    for x in values[1:]:
        result1-=x
    print(result1)
elif(c=="3"):
    result2=values[0]
    for y in values[1:]:
        result2=result2/y
    print(result2)
elif(c=="4"):
    result3=1
    for z in values:
        result3*=z
    print(result3)
