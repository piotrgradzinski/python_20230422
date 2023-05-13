"""
Write a program that prints a multiplication table for numbers from 0 to 10.

Sample output:

       0   1   2   3   4   5   6   7   8   9  10

0      0   0   0   0   0   0   0   0   0   0   0
1      0   1   2   3   4   5   6   7   8   9  10
2      0   2   4   6   8  10  12  14  16  18  20
3      0   3   6   9  12  15  18  21  24  27  30
4      0   4   8  12  16  20  24  28  32  36  40
5      0   5  10  15  20  25  30  35  40  45  50
6      0   6  12  18  24  30  36  42  48  54  60
7      0   7  14  21  28  35  42  49  56  63  70
8      0   8  16  24  32  40  48  56  64  72  80
9      0   9  18  27  36  45  54  63  72  81  90
10     0  10  20  30  40  50  60  70  80  90 100

simpler version:
0   0   0   0   0   0   0   0   0   0   0
0   1   2   3   4   5   6   7   8   9  10
0   2   4   6   8  10  12  14  16  18  20
0   3   6   9  12  15  18  21  24  27  30
0   4   8  12  16  20  24  28  32  36  40
0   5  10  15  20  25  30  35  40  45  50
0   6  12  18  24  30  36  42  48  54  60
0   7  14  21  28  35  42  49  56  63  70
0   8  16  24  32  40  48  56  64  72  80
0   9  18  27  36  45  54  63  72  81  90
0  10  20  30  40  50  60  70  80  90 100

We will need few features of a print function:
- print(10, end="")
- print(f"{a*b:4}")
- print() -> will print to the console only \n - new line

Hints:
- outer loop will be producing rows
- inner loop will be producing columns
"""

for a in range(0, 11):
    for b in range(0, 11):
        print(f"{a * b:4}", end='')
    print()

print()
print('Thank you very much!')
