#Prompt the user to enter an integer
integer=input("Please enter an integer:")
#Calculate the length of the integer
length=len(integer)
#Print every digit of the integer one by one
for i in range(0,length):
    print(integer[i])