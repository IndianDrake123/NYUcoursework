# Brian
# HW 1: Harmonic Analysis  
# Date Due: 9/22/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

from math import sin

frequency = float(input("Enter a value for the frequency, w: "))
duration = float(input("Enter a value for the duration fo hte sound wave, T: "))

amp_spectrum = (2 * sin(frequency * duration))/frequency

print("The amplitude spectrum of this Fourier transform is:", round(amp_spectrum, 3))