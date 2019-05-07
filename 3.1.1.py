#Check the n and l is available or not in gnu

gnu = []


gnu = raw_input("Enter : ")

	
if 'n' and 'l' in gnu:
	print("Both are Present") 
elif 'l' in gnu:
	print("l is Available ")
elif 'n' in gnu:
	print("n is Available")
else: 
	print("Not Available")



