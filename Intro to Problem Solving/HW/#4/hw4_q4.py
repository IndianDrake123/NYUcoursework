"""
Author: Brian Thomas 
Assignment / Part: HW4 - Q4 Lexicographic Trends
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

"""string = input("Enter a string of lowercase letters: ")
decreasing = True
location = 0
past_char = 123
for char in string:
    char = ord(char)
    if decreasing == True:
        if char < past_char:
            location += 1
            past_char = char
        else:
            decreasing = False

if decreasing == True:
    print(string, 'is decreasing')
else:
    print(string, 'is not decreasing')
    print(f'It stopped being lexicographically decreasing at location {location}')
"""
#I solved it using ord() function initially but realized it could not be used so I redid it without using #ord, but I wanted to save my first solution. 

string = input('Enter a string of lowercase letters: ')
location = 0
while location < len(string) - 1:
    if string[location] < string[location + 1]:
        print(string, 'is not decreasing. \nIt stopped being lexicographically decreasing at location', location + 1)
        location += len(string) + 1
    else:
        location += 1
        
if location == len(string) - 1:
    print(string, 'is decreasing')