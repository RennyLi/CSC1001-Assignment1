#Prompt up the indicator for users to enter the final account value
finalAccountValue=eval(input("Enter the final account value:"))

#Prompt up the indicator for users to enter the annual interest rate
annualInterestRate=eval(input("Enter the annual interest rate:"))

#Prompt up the indicator for users to enter the number of years
numberOfYears=eval(input("Enter the number of years:"))

#Calculat the initial deposit amount
m=(1+annualInterestRate/100)**numberOfYears
initialDepositAmount=finalAccountValue/m

#Display the result
print("The initial value is:",initialDepositAmount)