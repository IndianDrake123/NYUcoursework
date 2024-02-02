# Brian
# HW 2: Collective Timetables   
# Date Due: 9/22/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

Neha_days_worked = int(input("Enter the number of days Neha has worked: "))
Neha_hours_worked = int(input("Enter the number of hours Neha has worked: "))
Neha_minutes_worked = int(input("Enter the number of minutes Neha has worked: "))

Oleg_days_worked = int(input("Enter the number of days Oleg has worked: "))
Oleg_hours_worked = int(input("Enter the number of hours Oleg has worked: "))
Oleg_minutes_worked = int(input("Enter the number of minutes Oleg has worked"))

tot_days = Neha_days_worked + Oleg_days_worked
tot_hours = Neha_hours_worked + Oleg_hours_worked
tot_minutes = Neha_minutes_worked + Oleg_minutes_worked

print("THe total time both CAs worked together is:", tot_days, "days", tot_hours, "hours and", tot_minutes, "minutes")