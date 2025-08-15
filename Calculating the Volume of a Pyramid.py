# This script exectues a calculation to compute and print the volume of a 3D pyramid
# Given the formula of V=lwh/3 and a data table with 2 Test Cases the answers are computed and printed
# The answer is also rounded using 2 decimal places

# This is the mathematical formula used to execute the calculation
def pyramid_volume(length, width, height):
    return (length * width * height) / 3

# This lists the volume for Test Case 1 based on the given data table of variables and values
length1 = 7.0
width1 = 6.0
height1 = 9.0
volume1 = pyramid_volume(length1, width1, height1)
print(f"Test Case 1 Volume: {volume1:.2f}")

# This lists the volume for Test Case 2 based on the given data table of variables and values
length2 = 6.6
width2 = 3.3
height2 = 7.7
volume2 = pyramid_volume(length2, width2, height2)
print(f"Volume for Test Case 2: {volume2:.2f}")