#Consider the condition where the input is not a number
try:
    N=eval(input("Please enter a positive number:"))
except:
    print("Sorry, your input is invalid!")

if N<=0:
    print("Sorry, your input is invalid!")

#Print each row of the table
else:
    #Print the first line
    print("m     m+1   m**(m+1)")
    #Prin the corresponding numbers in each following line
    for row in range(1,N+1):
        print("%-6d"%row,"%-6d"%(row+1),"%-6d"%(row**(row+1)),sep="")