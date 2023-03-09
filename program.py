# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

for myNumber in range(1, 33):
    result = ""
    if myNumber % 3 == 0:
        result = result + "Fizz"
    if myNumber % 5 == 0:
        result = result + "Buzz"
    if myNumber % 5 != 0 and myNumber % 3 != 0:
        result = str(result) + str(myNumber) + "\n"
  
    print(result)

  #result = str(result) + str(myNumber) + "\n"

