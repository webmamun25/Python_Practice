"""
Write a Python program that creates a list of 5 numbers.
Ask the user for an index number and print the value at that index.
If the index is out of range, handle the exception and print "Invalid index!".
    """


try:
    listed_numbers = [2, 3, 4, 5, 6]
    n = int(input("Enter a number: "))
    print(listed_numbers[n])  # risky line
except Exception as e:
    print("Error:", e)
else:
    print("No error occurred!")
finally:
    print("The number is always here, must notice range is 0 to 4")