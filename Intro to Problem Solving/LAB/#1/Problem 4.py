days = int(input("days: "))
hours = int(input("hours: "))
minutes = int(input("minutes: "))
seconds = int(input("seconds: "))

total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

print(days, "Days", hours, "Hours", minutes, "Minutes and", seconds, "Seconds results in a total of", total_seconds, "Seconds")