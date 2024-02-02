import math

PI = 3.1416

scoops = float(input("scoops: "))
radius = float(input("radius: "))
height = float(input("height: "))

scoops_volume = scoops * 4/3 * PI * math.pow(radius, 3)
cone_volume = PI * math.pow(radius, 2) * (height/3)
total_volume = scoops_volume + cone_volume

print("your", int(scoops), "volume ice scream cone has a total volume of", total_volume)