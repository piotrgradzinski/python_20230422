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

"""
Type hinting is a technique of marking what data type arguments should have
and what data type will be returned from the function.
"""


def split_document_number_to_parts(document_number: str) -> dict:
    """
    Splitting document number string into a dictionary structure.
    For example document number "FV/BI/2023-1/10" will be parsed into:
    {"document_type": "FV", "department": "BI", "year": 2023, "quarter": 1, "number": 10 }.

    :param document_number: For example "FV/BI/2023-1/10"
    :return: Dictionary with document_type, department, year, quarter, number keys.
    """
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

for name, value in splitted_document_number.items():
    print(name, value)
