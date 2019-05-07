#Write the program to break the loop if user give n as input, if y continue



input1 = raw_input("Enter key : ")

def result(input1):
	for i in range(10):
		if input1 == 'y':
			pass
			print("loop is continue",i)
		elif input1 == 'n':
			break



x = result(input1)
print(x)
