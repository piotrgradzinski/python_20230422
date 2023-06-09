"""
We have two lists. One contains weights, second heights.
For each pair of weight and height calculate BMI.

Adjust the BMI formula as here we have heights in centimeters, not in meters.
https://en.wikipedia.org/wiki/Body_mass_index
BMI = weight / height ** 2
BMI = [kg] / [m]
"""

weights = [102, 150, 57, 128, 138, 56, 120, 53, 147, 119, 120, 114, 137, 79, 81, 94, 100, 88, 119, 93, 70, 112, 87, 56, 116, 138, 116, 111, 61, 117, 75, 85, 150, 120, 79, 66, 60, 127, 145, 121, 78, 140, 61, 106, 143, 142, 77, 147, 101, 87, 121, 124, 139, 80, 68, 90, 64, 102, 122, 61, 94, 86, 54, 72, 59, 89, 61, 101, 93, 65, 63, 113, 112, 77, 79, 89, 52, 124, 135, 50, 120, 109, 124, 57, 73, 54, 143, 52, 65, 63, 63, 119, 75, 70, 135, 123, 107, 102, 70, 82]
heights = [139, 186, 203, 200, 143, 218, 133, 213, 145, 141, 216, 126, 201, 196, 212, 209, 212, 211, 151, 183, 172, 204, 134, 125, 144, 152, 163, 208, 181, 205, 157, 194, 163, 120, 123, 130, 219, 218, 177, 132, 212, 202, 166, 198, 127, 158, 175, 186, 176, 130, 217, 198, 181, 218, 216, 148, 210, 200, 138, 156, 139, 125, 148, 137, 207, 179, 146, 134, 188, 165, 209, 193, 161, 134, 194, 136, 147, 194, 160, 167, 152, 138, 180, 137, 177, 185, 130, 124, 165, 126, 164, 180, 207, 120, 146, 213, 121, 181, 198, 175]

# convert heights from cm to m
heights_m = map(lambda height: height / 100, heights)

# calculate BMIs
bmis = map(lambda weight, height: weight / height ** 2, weights, heights_m)
bmis = list(bmis)  # to avoid empty iterator in the filter part

for bmi in bmis:
    print(round(bmi, 2))

# filter bmis to get only those values which are in a "Normal range" - 18.5 – 24.9
normal_range = filter(lambda bmi: 18.5 < bmi < 24.9, bmis)
normal_range = list(normal_range)
normal_range.sort()

print('Normal range')
for bmi in normal_range:
    print(round(bmi, 2))

