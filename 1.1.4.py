#Find the given input as string|integer|float using type() and str|int|float|bool

x = input("Enter Integer Input : ")
print("Integer is And Type : ",type(x),x)


y = raw_input("Enter The String : ")
print("String Is And Type: ",type(y),y)

z = float(input("Enter The Float value : "))
print("Float Value Is And Type : ",type(z),z)

t = bool(input("enter input : "))
print(type(t))
