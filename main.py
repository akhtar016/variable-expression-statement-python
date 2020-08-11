# Print something
print('Hello World')

# Take input, put it in the variable and print it
userName = input('Enter Your Name: ')
print('Hello ' + userName)
print(f'Hello {userName}')

# Exercise 1 : Convert elevator floors
inp = input("Europe floor? ")
usf = int(inp) + 1
print('US floor ', usf)

# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
name = input("Enter your name: ")
print("Hello ", name)

#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay

numOfHours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = int(numOfHours) * int(rate);
print("Pay: ", pay)

""" #Exercise 4: Assume that we execute the following assignment statement:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the type
1. width//2
2. width/2.0
3. height/3
4. 1 + 2 \* 5
 """
width = 17
height = 12.0

print("width // 2 :", width//2)
print("width/2.0 : ", width/2.0)
print('height/3 : ', height/3)
#print('1 + 2\*5 :', 1 + 2 \* 5)

""" Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
    and print out the converted temperature.
"""

celsiusTemp = input("Enter temperature in Celsius: ")
fahrenheit = int(celsiusTemp) * (9 / 5) + 32
print(f'Fahrenheit of {celsiusTemp} is {fahrenheit}')

