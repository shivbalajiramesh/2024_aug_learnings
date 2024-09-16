#Age = int(input("Please enter your age: "))
Age = 0

if Age > 18:
     print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Number = int(input("Enter a number: "))
Number = 0


if (Number%3 == 0) and (Number%5 == 0):
    print("The number is divisible by 3 and 5.")
else:
    print("The number is not divisible by 3 and 5")


Numbertwo = int(input("Enter a number: "))


if (Numbertwo%2 == 0):
    print("The number is even.")
elif (Numbertwo%2 == 1):
    print("The number is odd")


Salary = int(input("Enter your Salary: "))
Age = int(input("Enter your Age: "))

if Salary >= 20000 or Age <= 25:
          loan_amount = int(input("How much loan do you want: "))
          if loan_amount <= 50000:
                            print("You are eligible")
          else:
              print("Max Loan amount is 50000")
else:
    print("You are not eligible for loan")


    
            
        
