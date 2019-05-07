#Use list functions append(), count(), extend(), index(), insert(), pop(), remove(), reverse() and sort()


#append(),count()
limit = int(input("Enter Last Limit Of List : "))
List1 = []
for i in range(limit):
	List1.append(raw_input(' '))
print(List1)
print("Count Of Name", List1.count(raw_input("Enter Name Which We Want To Count  : ")))

print("List Element : ",List1)

#extend() function.

List1 = ['ganesh','nilesh','sumit']
List2 = ['himanshu','shohib']
List1.extend(List2)
print("Extended List : ",List1)


#index()

List1 = ['python','c','cpp','embedded c','linux','tcp/ip']
print(List1)
print(List1.index(raw_input("Enter Which Index we Want To Know : ")))

#insert()

List1 = ['camera','tracor','netgear']
print("Old List Element : ",List1)
List1.insert(3,raw_input(' '))
print("New List Element : ",List1)

#pop()

list1 = ['a','b','c','d','e','f']
print(list1)
list1.pop(int(input("Enter index  Number Which We Want To Remove: ")))
print("POP Element List : ",list1)

#remove()
List1 = ['python','c','cpp','embedded c','linux','tcp/ip']
print(List1)
List1.remove(raw_input("Enter List Element Which We Want To Remove: "))
print("Remove Element List : ",List1)


#reverse
List1 = [1,2,3,4,5,6]
List1.reverse()
print(List1)

#sort

List1 = [4,2,8,6,4,2,0]
List1.sort()
print(List1)




