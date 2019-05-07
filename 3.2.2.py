#Write the program to get the name of user and reverse it



name = []
name = raw_input("Enter The Name : ")
print("Original",name)
reverse = name[::-1]
print("Reverse",reverse)


len1 = len(name)
print("Length of String",len1)
i = len1-1




while i >= 0:
	print(name[i])	
	i = i - 1

