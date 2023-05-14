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
    if document_number.count('/') != 3:
        # approach with raising exception
        raise ValueError('Document number must contain 4 parts in a format ex. FV/BI/2023-1/10')
    
    segments = document_number.split('/')

    return {
        'document_type': segments[0],
        'department': segments[1],
        'year': int(segments[2].split('-')[0]),
        'quarter': int(segments[2].split('-')[1]),
        'number': int(segments[3])
    }


try:
    users_document_number = input('Provide document number: ')
    splitted_document_number = split_document_number_to_parts(users_document_number)
    print(splitted_document_number)

    for name, value in splitted_document_number.items():
        print(name, value)
except ValueError:
    print('Hey, you have provided wrong document number. ')
    print('It should be like this: FV/BI/2023-1/10')
except KeyError:
    print('Handling another exception')
