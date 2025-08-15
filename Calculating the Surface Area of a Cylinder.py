# This script exectues a calculation to compute and print the volume of a 3D pyramid
# Given the formula of A=2πrh+2πr2 and a data table with 2 Test Cases the answers are computed and printed
# The answer is also rounded using 2 decimal places

# This imports the math for pi
import math

# This lists the surface area for Test Case 1 based on the given data table of variables and values
radius1 = 6
height1 = 9

# This calculates the surface area for the 1st cylinder with 2 decimal places
area1 = 2 * math.pi * radius1 * height1 + 2 * math.pi * radius1 * radius1
print("Surface Area 1: {:.2f}".format(area1))

# This lists the surface area for Test Case 2 based on the given data table of variables and values
radius2 = 2
height2 = 10

# This calculates the surface area for the 2nd cylinder with 2 decimal places
area2 = 2 * math.pi * radius2 * height2 + 2 * math.pi * radius2 * radius2
print("Surface Area 2: {:.2f}".format(area2))