"""
Author: Brian Thomas 
Assignment / Part: HW6 - Q1 Final Grade
Date due: November 2, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def calculate_grade(assignment_score, midterm_score, final_score):
    grade = assignment_score * .4 + midterm_score * .3 + final_score * .3
    return grade

def get_valid_score(prompt):
    grade = input(f'Enter a score for {prompt}: ')
    while not grade.isdigit():
        print("Invalid, Enter a numeric value between 0 and 100.")
        grade = input(f'Enter a score for {prompt}: ')

    return float(grade)

def display_result(grade):
    if grade >= 90:
        remark = 'Outstanding performance'
    elif grade >= 80:
        remark = 'Good work'
    elif grade >= 70:
        remark = 'Can improve'
    elif grade >= 60:
        remark = 'Passed'
    else:
        remark = 'Failed'

    print(f'Grade:{grade:.2f}. {remark}')

def main():
    assignment_score = get_valid_score("Assignments")
    midterm_score = get_valid_score("Midterm")
    final_score = get_valid_score("Final")
    calculated_grade = calculate_grade(assignment_score, midterm_score, final_score)
    display_result(calculated_grade)
