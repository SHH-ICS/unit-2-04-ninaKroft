# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

#fizzbuzz = 0

for num in range(32):
    result = ""
    if num % 3 == 0:
        result = result + "Fizz"
    if num % 5 == 0:
        result = result + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        result = result + str(num)
    print(result)

  #result = str(result) + str(myNumber) + "\n"

#print(result)
