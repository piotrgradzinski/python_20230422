"""
Create the following package and module structure:
- main mathematica package
- internal geometry package
- the figures module in the geometry package with the functions
    - square_area and triangle_area
- Internal algebra package
- formulas module in the algebra package with the following functions
    - add, subtract, multiply, divide
- tests/test_algebra module testing algebraic functions
- tests/test_geometry module testing geometric functions

Directory and file structure:
mathematica/
    algebra/
        formulas.py
    geometry/
        figures.py

At the level of the directory where the mathematica package is located, create the file
usage_of_mathematica and, using the various import methods, run the functions:
square_area, triangle_area, multiply.
"""