#1 reverse using function
def reverse(string):
     return string[::-1]
str =input("enter a string")
print(reverse(str))


#simple reverse
string=input("enter a string")
print(string[::-1])




#reverse string using reverse and join function
def reverse(string):
	string = list(string)
	string.reverse()
	return "".join(string)

str=input()
print(reverse(str))






