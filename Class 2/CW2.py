
#Understanding Arithmetic Operators
'''
number_one = int(input("Enter a number: "))
number_two = int(input("Enter a number: "))

addition = number_one+number_two
print("The sum is", addition)

subtraction = number_one-number_two
print("The difference is", subtraction)

multiplication = number_one*number_two
print("The product is", multiplication)

division = number_one/number_two
print("The quotient is" , division)

quotient = number_one//number_two
print("The quotient is", quotient)

remainder = number_one%number_two
print("The remainder is", remainder)

power = number_one**number_two
print(number_one, "to the power of ", number_two, " is ", power)

#Arithmetic Operators with String Data Type

num_one = str(input("Enter anything: "))
num_two = str(input("Enter anything: "))

add = num_one+num_two #concatenation
print("The sum is ", add)

multiply = num_one*2 
print("Your first value multiplied by two is ", multiply)

#Calculating Simple Interest

principal = int(input("What is the Principal Amount?"))
rate = int(input("What is the rate?"))
time = int(input("What is the duration in years?"))

simple_interest = (principal*rate*time)/100
print("The simple interest is: ", simple_interest)

amount = simple_interest+principal
print("The total amount is: ", amount)

#Calculating Compund Interest

p = int(input("What is the Principal Amount?"))
r = int(input("What is the rate?"))
t = int(input("What is the duration in years?"))

a = p*(1+r/100)**t
print("The amount is", a)

compound_interest = a-p
print("The compund interest is", compound_interest)

#Activity 1

temperature = int(input("What is the temperature outside?"))

if (temperature>30):
    print("It's a hot day")
else:
    print("It is a pleasant day.")
'''
#Activity Two

n_one = int(input("Enter a number"))
n_two = int(input("Enter another number"))

if n_one == n_two:
    print("They are equal")
elif n_one != n_two:
    print("They are not equal")
if n_one> n_two:
    print("Your first number is greater than the second")
elif n_one<n_two:
    print("Your first number is smaller than your second number")
#greater or equal
#less or equal

                               