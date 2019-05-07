#Write the program to replace the odd position string with X on any strings

string = []
string1 = ['x']
string = raw_input("Enter The String : ")
len1 = len(string)
i = 0
while i <= len1-1:
	if i%2 != 0:
		string.index(string1)
	i = i+1
print(string)
