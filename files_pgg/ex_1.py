"""
Write a programme which prints out the contents of the indicated file
with line numbers to the console.
You can leverage test.txt file.

Sample output:
1: To be or not to be
2: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
3: Duis tellus odio, hendrerit ut est id, convallis scelerisque eros.
4: Mauris quis sem volutpat, scelerisque dolor et, efficitur ex.
5: Nulla id tortor id mi faucibus dignissim. Curabitur bibendum sem erat.
6: Maecenas faucibus tortor ac pulvinar sollicitudin. Donec nec semper elit.
7: Cras in urna tellus. Donec velit enim, finibus in mauris ornare, luctus tempor nunc.
8: Sed sed arcu in nisl tempor porta.
"""

with open('test.txt', 'r', encoding='utf-8') as file_handle:
    # approach 1
    line_number = 1
    while True:
        line = file_handle.readline()
        if not line:
            break
        print(f"{line_number}: {line.rstrip()}")
        line_number += 1

    print('-' * 30)

    # approach 2
    file_handle.seek(0)  # rewind the pointer to the beginning of the file
    line_number = 1
    for line in file_handle:
        print(f"{line_number}: {line.rstrip()}")
        line_number += 1

    print('-' * 30)

    # approach 3
    file_handle.seek(0)
    for line_number, line in enumerate(file_handle, start=1):
        print(f"{line_number}: {line.rstrip()}")
