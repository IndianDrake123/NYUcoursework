"""
Author: Brian Thomas 
Assignment / Part: HW8 - Q4 GradescopeTM Logic
Date due: November 16, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

from statistics import mean, stdev, median

def get_list_of_grades(grades_filepath):
    try:
        file = open(grades_filepath, "r")
    except FileNotFoundError:
        return 0
    
    header = file.readline().split(',')
    content = file.readlines()
    grades_list = []

    pos = 0
    for i in range(5, len(header)):
        grades_list.append([])
        for line in content:
            values = line.strip('\n').split(',')
            if values[2] == "Graded":
                grades_list[pos].append(float(values[i]))
        pos += 1

    file.close()
    return grades_list

def generate_statistics_report(grades_filepath, stats_filepath):
    grades = get_list_of_grades(grades_filepath)
    with open(stats_filepath, "w") as file:
        file.write("Mean,Standard Deviation,Median\n")
        for line in grades:
            file.write(f"{round(mean(line), 2)},{round(stdev(line), 2)},{round(median(line), 2)}\n")

def main():
    generate_statistics_report("Midterm1_scores.csv", "stats.csv")

main()