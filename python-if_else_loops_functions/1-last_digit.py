#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of{number}", end ="")
the_last_digit = number % 10
print(f"is{the_last_digit}", end ="")

if the_last_digit > 5 :
    print("and is greater than 5")
    print("\n")

elif the_last_digit == 0 : 
    print ("and is 0")
    print("\n")
    
elif the_last_digit < 6 and not 0 :
    print ("and is less than 6 and not 0")
    print("\n")