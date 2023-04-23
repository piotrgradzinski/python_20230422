"""
https://drive.google.com/file/d/1oVMo8BT8igl_ri0lAACn2R434xA30Xxx/view?usp=sharing

Write a program that, based on the player’s position (x, y) on the board
in the range from 0 to 100,
displays its approximate location (center, upper right corner, upper edge, ...)
or information about the position outside the board. Take the value 10 as an edge margin.

Sample program output:
Enter player's X position: 95
Enter player's Y position: 95
The player is in the upper right corner.
"""

x = int(input('Enter player\'s X position: '))
y = int(input('Enter player\'s Y position: '))

if 0 <= x <= 10:
    if 0 <= y <= 10:
        print('left bottom corner')
    elif 10 < y < 90:
        print('left side')
    elif 90 <= y <= 100:
        print('left top corner')
    else:
        print('You are out of the board.')
elif 10 < x < 90:
    if 0 <= y <= 10:
        print('bottom side')
    elif 10 < y < 90:
        print('center')
    elif 90 <= y <= 100:
        print('top side')
    else:
        print('You are out of the board.')
elif 90 <= x <= 100:
    if 0 <= y <= 10:
        print('right bottom corner')
    elif 10 < y < 90:
        print('right side')
    elif 90 <= y <= 100:
        print('right top corner')
    else:
        print('You are out of the board.')
else:
    print('You are out of the board.')
