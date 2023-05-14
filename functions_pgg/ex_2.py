"""
Write a function that will get document a number as an argument
(in this format "FV/BI/2023-1/10") and will return a dictionary
containing elements of this number.

Number consists of:
document type/department/year-quarter/number

Example:
split_document_number_to_parts("FV/BI/2023-1/10")

returns
{
    "document_type": "FV",
    "department": "BI",
    "year": 2023,
    "quarter": 1,
    "number": 10
}
"""


def split_document_number_to_parts(document_number):
    segments = document_number.split('/')

    return {
        'document_type': segments[0],
        'department': segments[1],
        'year': int(segments[2].split('-')[0]),
        'quarter': int(segments[2].split('-')[1]),
        'number': int(segments[3])
    }


splitted_document_number = split_document_number_to_parts("FV/BI/2023-1/10")
print(splitted_document_number)
