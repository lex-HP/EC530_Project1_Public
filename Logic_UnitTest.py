import MatrixMulti
import numpy as np
import random

# THIS IS THE LOGIC TEST NOT INPUT TEST
# testcases to check if math in MatrixMulti.matmul is correct,
# assumes input are correct, on failure Exception is raised and returns 0


# Alternate between two MatrixMulti functions, defaults to matmul if not set.
func2call = MatrixMulti.matmul


def set_func2call(choice):
    global func2call
    if choice == 0:
        func2call = MatrixMulti.matmul
    if choice == 1:
        func2call = MatrixMulti.matrix_multiplication

# Used in testing_logic, convert list of list into np.array
# with float64 items (allclose crash otherwise) and use numpy to compare


def check_isequal(a, b):
    Calculated_result = np.array(func2call(a, b), dtype=np.float64)
    Expected_result = np.matmul(np.array(a), np.array(b))
    Expected_result = Expected_result.astype(np.float64)
    return np.allclose(Calculated_result, Expected_result, atol=1e-30)


def testing_logic():
    try:

        a = [[2, 4, 2], [5, 7, 5]]
        b = [[5, 6], [7, 8], [12, 14]]
        if not check_isequal(a, b):  # Standard test 1
            raise Exception("Standard test 1 failed")

        a = [[23, 48, 22], [55, 70, 43], [76, 356, 98]]
        b = [[5, 84], [7, 834], [12, 140]]
        if not check_isequal(a, b):  # Standard test 2
            raise Exception("Standard test 2 failed")

        a = [[23, 48, 22], [55, 70, 43], [76, 356, 98]]
        b = [[5], [12], [0]]
        if not check_isequal(a, b):  # Standard test 3
            raise Exception("Standard test 3 failed")

        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if not check_isequal(a, b):  # Zero matrix test
            raise Exception("Zero matrix test failed")

        a = [[23345678765432456, 486534567890987654432, 228654321234567876543],
             [5587698765432543, 7023498765436, 234568765434543]]
        b = [[5234598764234566, 8987654323440987],
             [709876542346, 839874654567898765],
             [121876543234, 140987657890765]]
        if not check_isequal(a, b):  # Big integers test
            raise Exception("Big integers test failed")

        a = [[23.4, 48.7, 22.0], [55.5, 70.23, 43.1]]
        b = [[5.44, 84.65], [7.4, 834.5], [12.54, 140.23]]
        if not check_isequal(a, b):  # Float test
            raise Exception("Float test failed")

        a = [[23.47654321, 48.7987654, 22.098765], [
            55.5876543, 7087654321.23, 8763.187654321]]
        b = [[5.4445678, 84.687655], [7.4876, 834.59875432],
             [12.54651234, 140.2876543]]
        if not check_isequal(a, b):  # Large float test
            raise Exception("Large float test failed")

        a = [[2765432123453.4764321, 4765432234568.79876, 287654323452.098765],
             [587654323455.5876543, 7087654321.23, 8787654363.187654321]]
        b = [[8765432765435.4445678, 8876543223454.687655],
             [9876542234567.4876, 83765432123454.59875432],
             [16543234562.54651234, 14765432123456780.2876543]]
        if not check_isequal(a, b):  # Big Integer + large float failed
            raise Exception("Big Integer + large float failed")

        a = [[-65, -234, 253], [-123, 7, -5]]
        b = [[5, -6], [-7, 765], [12, -14]]
        if not check_isequal(a, b):  # Negative integer test
            raise Exception("Negative integer test failed")

        a = [[-60.42, -239.56, 2.76], [-12.78, 722.23, -1.67]]
        b = [[52.34, -65.89], [-7.6, 765.4], [123.67, -14.56]]
        if not check_isequal(a, b):  # Negative integer with float test
            raise Exception("Negative integer with float test failed")

        a = [[-2345678765432.4566543234567, 486534567890987654432.987654321, 228654321234567876543.5432165432127654],
             [5587698765432.543765432, -7023498765436.12346543212345, 234568765434543.6789876543234567]]
        b = [[523459876423456.698765432234567, 898765432344.09876543287],
             [709876542346.9987654321876, -839874654567898765.654765432345632],
             [121876543234.965432345678765487, -140987657890765.128765432134]]
        if not check_isequal(a, b):  # Big negative int with large float test
            raise Exception(
                "Big negative integer with large float test failed")

        # random large dimmensions for matrix test.
        Test_Amount = 5
        MaxMatSize = 400
        print('Info: Oversized Matrices start for ', Test_Amount,
              ' rounds. Maximum size set at: ', MaxMatSize, '*', MaxMatSize)
        for i in range(Test_Amount):
            rowA_amount = random.randint(1, MaxMatSize)
            colB_amount = random.randint(1, MaxMatSize)
            colA_rowB_amount = random.randint(1, MaxMatSize)
            print('Info: Big Matrices round ', i+1, 'out of', Test_Amount,
                  '| Dimensions: (', rowA_amount, ',', colA_rowB_amount, ')X(',
                  colA_rowB_amount, ',', colB_amount, ')', end=' ', flush=True)

            a = [[random.uniform(-10000.00000, 100000.00000)
                  for rows in range(colA_rowB_amount)] for cols in range(rowA_amount)]
            b = [[random.uniform(-10000.00000, 100000.00000)
                  for rows in range(colB_amount)] for cols in range(colA_rowB_amount)]
            if not check_isequal(a, b):  # Matrix dimension test
                raise Exception("Matrix Dimension test failed")
            print('DONE')
        print("~~~~~~~~~~~~~~ All Logic tests passed ~~~~~~~~~~~~~~")
        return 1

    except Exception as out:
        print(out)
        return 0


if __name__ == "__main__":
    testing_logic()
