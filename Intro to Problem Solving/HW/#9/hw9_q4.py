"""
Author: Brian Thomas 
Assignment / Part: HW9 - Q4 Merge Intervals
Date due: November 30, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def merge_intervals(lst):
    lst.sort() 
    merged_lst = [lst[0]]
    for rnge in lst[1:]:
        current_lower_bound, current_upper_bound = rnge
        previous_lower_bound, previous_upper_bound = merged_lst[-1]
        if current_lower_bound <= previous_upper_bound:
            merged_lst[-1] = (previous_lower_bound, max(current_upper_bound, previous_upper_bound))
        else:
            merged_lst.append(rnge)

    return merged_lst

def main():
    lst = ([(1, 3), (2, 6), (5, 10), (7, 12), (15, 18)])
    merged_intervals = merge_intervals(lst)
    print(merged_intervals)

main()