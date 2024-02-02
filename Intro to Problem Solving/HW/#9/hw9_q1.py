"""
Author: Brian Thomas 
Assignment / Part: HW9 - Q1 Club Assignment Algorithm
Date due: November 30, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def group_students(clubs, students):
    final_assignment = []

    for club in clubs:
        members = []
        for student in students:
            if student[1] == club[0] and len(members) < club[1]:
                members.append(student[0])
        final_assignment.append(members)
    
    return final_assignment

def main():
    club_specs = [("Chess Club", 15), ("Art Club", 20), ("Writing Club", 3)]
    student_prefs = [
("Alice", "Chess Club"),
("Bob", "Chess Club"),
("Flora", "Writing Club"),
("Charlie", "Art Club"),
("David", "Writing Club"),
("Melody", "Writing Club"),
("Ana", "Writing Club")
]
    print(group_students(club_specs, student_prefs))

main()