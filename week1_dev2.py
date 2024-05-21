# FizzBuzz Challenge
# =======================
""" This script prints out numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
It uses a simple loop and conditional statements to achieve this."""

# Author: Ibrahim Yisau
# Date: 21-May-2024

# Loop through numbers 1 to 100
for i in range(1, 101):
	# Check if the number is divisible by 3
	if i % 3 == 0:
		# Print "Fizz" if it is
		print("Fizz")
	# Check if the number is divisible by 5
	elif i % 5 == 0:
		# Print "Buzz" if it is
		print("Buzz")
	# Check if the number is divisible by both 3 and 5
	elif i % 3 == 0 and i % 5 == 0:
		# Print "FizzBuzz" if it is
		print("FizzBuzz")
	# If none of the above conditions are met, print the number
	else:
	    print(i)
        
