number=eval(input("Enter a positive number:m="))
#Prompt the user to input a number m

integer=0
#Iterate from 0 to the correct answer

while(True):
#Avoid the condition where the while loop is false and meaningless
    if integer**2>number:
        print("n=",integer,sep="")  #Display the result
        break  #Stop the while loop
    integer=integer+1
    #Continue to look for the correct answer