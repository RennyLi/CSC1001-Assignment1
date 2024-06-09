#Handle the possible improper inputs
try:
    N=eval(input("Please enter an integer(integer>2):N="))
except:
    N=None
if N is None:
    print("The input is invalid!")
else:
    count=0
    #Count the total prime numbers
    print("The prime numbers smaller than",N,"include:")
    #Print the first line

    for number in range(2,N):
        isPrime=True
        #The number is a prime number
        for devisor in range(2,number):
            if number%devisor==0:
                isPrime=False
                #In this case, the number is not a prime number

        if isPrime:
            count+=1
            #When it's a prime number, count it into the total prime number
            print(number,end="\t")
            #Print corresponding prime number and display them into a chart

            if count%8==0:
                print("")
                #Output at most 8 prime numbers in each line
            
            