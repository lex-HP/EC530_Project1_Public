# EC530_Assignment1 Matrix Multiplication
## Alex Hureaux-Perron U69933875 alexchp@bu.edu lex-HP
This repository has purpose to teach us on how to use github action and unit testing
This assignment has 3 important parts: 
- Matrix Multiplication
- Unit testing of Matrix Multiplication
- Workflows

## Matrix Multiplication
The python file [MatrixMulti.py](MatrixMulti.py) has three functions whose purpose is to take in 2 lists of lists of floats and returns either the result of A X B or an exception on input failures. Those three functions have distinct jobs:
- MatrixMulti.matmul(MatA, MatB) --> Does A X B and returns the result, assumes inputs are always correct
- MatrixMulti.input_error_check(MatA, MatB) --> Check input type and correct matrix size, returns 1 on correct input or exception on wrong input. 
- MatrixMulti.matrix_multiplication(MatA, MatB) --> serves as main, fuses matmul and input_error_check together. Returns either the result of A X B or an exception on input failures.
At the demand of the teacher, numpy is not used in this code. Therefore arrays are not supported!

## Unit testing of Matrix Multiplication
Since MatrixMulti.py has three functions to test, there are three test files:
- [Logic_UnitTest.py](Logic_UnitTest.py) checks matmul ability to output the correct result by comparing it to numpy operator. It has 11 different fixed tests as well as a loop checking multiple random big inputs. On success, returns 1. On failure, returns 0 and print exception. 
- [Input_UnitTest.py](Input_UnitTest.py) checks input_error_check ability to detect if an input is correct or not. It has 13 different fixed tests. On success, returns 1. On failure, returns 0 and print exception.
- [Main_UnitTest.py](Main_UnitTest.py) checks matrix_multiplication ability to detect wrong inputs and ability to output the correct result. It uses the same unit test set as Logic_UnitTest and Input_UnitTest. Therefore checking 13 + 11 = 24 fixed test and multiple large matrices inputs. On success, returns the result of A X B. On failure, returns assertion error. The errors specify which part failed. 

## Workflows
Two workflows in github action:
- Flake8 linter --> Lints the code and fail if not up to standard, note that complexity was increased to 17 due to the unit tests being long.
- Python matrix multiplication testing --> runs "pytest Main_UnitTest.py" in a container. Fail if Assertion error in Main_UnitTest is triggered




