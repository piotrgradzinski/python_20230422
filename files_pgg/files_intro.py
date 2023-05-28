"""
Files

How do we work with files:
1 we need to open a file in a certain mode and get "file handle"
2 work with the file: read, write, append...
3 we need to close the file handle / file - it's very common operation with different external (to our program) resources

Modes:
https://stackoverflow.com/a/16212401/779084
https://docs.python.org/3/library/functions.html#open
"""

# 1 step
# file_handle = open('test.txt')
# relative paths - relative to files_intro.py file
# .. - go one level (directory) up
# file_handle = open('../test2.txt')

# absolute path
# file_handle = open('/Users/gradzinski/dev_home/alx_python/szkolenia/2023_04_ZDL_Z/python_20230422/test2.txt')

file_handle = open('test.txt')

# 2 step
file_content = file_handle.read()
print(file_content)

# 3 step
file_handle.close()

print('-' * 30)

# modes are really important and based on the mode you have your file opened in you can or can't do some operations
# file_handle = open('test.txt', 'w')
# file_handle.write('To be or not to be')
# file_handle.close()

print('-' * 30)

"""
To make Python close the file for us automatically, we can use compound statement.
"""

with open('test.txt', 'r', encoding='utf-8') as file_handle:
# with open('../collections_pgg/collections_intro.py', 'r', encoding='utf-8') as file_handle:
    file_content = file_handle.read()
    print(file_content)
    print(file_handle.closed)  # False
    print(file_handle.encoding)  # utf-8
    print(file_handle.mode)  # r
    print(file_handle.name)  # test.txt
    print(file_handle.readable())  # True
    print(file_handle.writable())  # False

    file_handle.seek(0)  # moves the internal pointer to the beginning of the file
    file_content = file_handle.read()
    print(file_content)

    file_handle.seek(0)
    print(file_handle.read(15))

    print('-' * 10)

    file_handle.seek(0)
    print(file_handle.readline().rstrip())  # by default when we have new line character at the end of the line in a file - it's also read.
    print(file_handle.readline())
    print(file_handle.readline())

    print('-' * 10)

    file_handle.seek(0)
    lines = file_handle.readlines()  # list of lines from the file
    print(lines)

    print('-' * 10)

    file_handle.seek(0)
    for line in file_handle:
        print(line)


# once we leave the compound statement Python will close the file automatically.
print(file_handle.closed)  # True
