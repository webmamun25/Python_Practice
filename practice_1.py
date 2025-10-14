""" 
Problem 1: Common Friends (Set Operations)
Problem:
 Given two sets of friends from two people, find the mutual friends, unique friends of each, and the total number of unique friends.
Example Input:
a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

Expected Output:
Mutual friends: {'Sakib', 'Jamal'}
Unique to A: {'Rahim', 'Karim'}
Unique to B: {'Rafiq', 'Nadim'}
Total unique friends: 6


"""

a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

Mutual_friends=(a_friends&b_friends)
print(f"Mutual Friends:{Mutual_friends}")
Unique_to_A=a_friends-b_friends
print(f"Unique to A:{Unique_to_A}")
Unique_to_B=b_friends-a_friends
print(f"Unique to B:{Unique_to_B}")

""" 
Problem 2: Sort Students by Marks (Tuple + Dictionary)
Problem:
You are given a list of tuples — each containing a student’s name and mark.
Sort them in descending order of marks and print the top 3 scorers.
Example Input:
students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]

Expected Output:
Top 3 students:
Anik - 98
Sumi - 95
Hasan - 90

"""

students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]

sorted_array=sorted(students,key=lambda x :x[1],reverse=True)
print(sorted_array)
top_3 = sorted_array[:3]
print(top_3)
# Print result
print("Top 3 students:")
for name, mark in top_3:
    print(f"{name} - {mark}")



""" 
Problem 3: Word Length Filter (Lambda + Filter)
Problem:
 Given a list of words, use filter() and lambda to return only words whose length is greater than 4.
 Example Input:
words = ["sun", "planet", "moon", "star", "universe"]

Expected Output:
['planet', 'universe']


"""


words = ["sun", "planet", "moon", "star", "universe"]

filtered_words=list(filter(lambda x:len(x)>4,words))
print(filtered_words)


""" 
Problem 4: Square of Even Numbers (Map + Filter + Lambda)
Problem:
 Write a one-line Python expression using map(), filter(), and lambda that takes a list of integers and returns the squares of even numbers only.
Example Input:
nums = [1, 2, 3, 4, 5, 6]

Expected Output:
[4, 16, 36]

"""
nums = [1, 2, 3, 4, 5, 6]

filtered_numbers=list(filter(lambda x:x%2==0,nums))

square_numbers=list(map(lambda x:x**2,filtered_numbers))
print(square_numbers)

""" 
Create a text file named data.txt


Write “Learning Python is fun!” into it.


Read the file and print its content.

"""

with open("data.txt",'w+') as file:
    
    file.write("Learning Python is fun!")
    file.seek(0)
    lines=file.read()
    print(lines)


""" 
 Problem 6: Count Lines in a File
Problem:
 Write a Python program to count how many lines are in a text file named story.txt.
 If the file does not exist, handle the exception and print an error message, otherwise read the text file ( test it with both conditions ). Print a message finally. 

"""
try:
    # Try to open the file in read mode
    with open("story.txt", "r") as file:
        lines = file.readlines()
        print("Number of lines in the file:", len(lines))

except FileNotFoundError:
    # If file doesn't exist
    print("Error: The file 'story.txt' was not found!")

except Exception as e:
    # Catch any other unexpected errors
    print("An error occurred:", e)

finally:
    # This block always runs — success or failure
    print("File line counting operation completed.")