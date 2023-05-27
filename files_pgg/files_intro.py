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
file_handle = open('/Users/gradzinski/dev_home/alx_python/szkolenia/2023_04_ZDL_Z/python_20230422/test2.txt')

# 2 step
file_content = file_handle.read()
print(file_content)

# 3 step
file_handle.close()

print('-' * 30)

# modes are really important and based on the mode you have your file opened in you can or can't do some operations
file_handle = open('test.txt', 'w')
file_handle.write('To be or not to be')
file_handle.close()
