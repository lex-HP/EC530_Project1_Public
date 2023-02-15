import MatrixMulti
# Checks inputs format and type for MatrixMulti.input_error_check,
# returns 1 on all test passed, returns 0 on fail.

# Alternate between two MatrixMulti functions,
# defaults to input_error_check if not set.
func2call = MatrixMulti.input_error_check


def set_func2call(choice):
    global func2call
    if choice == 0:
        func2call = MatrixMulti.input_error_check
    if choice == 1:
        func2call = MatrixMulti.matrix_multiplication


def correct_input(a, b):
    return func2call(a, b)


def testing_input():
    try:

        a = [[2, 4, 2], [5, 7, 5]]
        b = [[5, 6], [7, 8], [12, 14]]
        if not correct_input(a, b):  # Standard test
            raise Exception("Integer only test failed")

        a = [[2, 4, 2], [-5, 7, 5]]
        b = [[5, 0], [7, 8], [12.121212, 14]]
        if not correct_input(a, b):  # Float + negative test
            raise Exception("Float + negatives test failed")

        a = [[2]]
        b = [[5]]
        if not correct_input(a, b):  # 1 by 1 test
            raise Exception("1 by 1 test failed")

        a = [[2, '4', 2], [5, 7, 5]]
        b = [[5, 6], [7, 8], [12, 14]]
        if not correct_input(a, b):  # Char item test
            raise Exception("Char item test failed")

        a = [[2, 87, 2], [5, 7, 5]]
        b = [[5, "Hello World"], [7, 8], [12, 14]]
        if not correct_input(a, b):  # String item test
            raise Exception("String item test failed")

        a = [[]]
        b = [[]]
        if not correct_input(a, b):  # Emtpy item test
            raise Exception("String item test failed")

        a = [[2, 4, 2], [5, 7, 5]]
        b = [[5, 6], [7, 8], [float('nan'), 14]]
        if not correct_input(a, b):  # NaN test
            raise Exception("NaN test failed")

        a = [['wert', 'c', 'kjhgfd'], ['hgfd', '543', 'hgf']]
        b = [['hgfds', 'dfghj'], ['654e', 'hgfds'], ['ujtr', 'gfdety']]
        if not correct_input(a, b):  # All items are char or string
            raise Exception("All char or string test failed")

        a = [[2, 4 + 3j, 2], [5, 7, 5]]
        b = [[5, 6], [7, 8], [12, 14]]
        if not correct_input(a, b):  # Complex number test
            raise Exception("Complex number test failed")

        a = [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[9, 10, 11], [12, 13, 14], [
            15, 16, 17]], [[18, 19, 20], [21, 22, 23], [24, 25, 26]]]
        b = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [
            16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
        if not correct_input(a, b):  # 3d Matrice test failed
            raise Exception("3D Matrice test failed")

        a = [[2, 4, 2], [5, 7, 5, 6]]
        b = [[5, 6], [7, 8], [12, 14]]
        if not correct_input(a, b):  # Dimension test 1
            raise Exception("Dimension test 1 failed")

        a = [[2, 4, 2], [5, 7, 5]]
        b = [[5, 6], [7, 8], [12, 14], [5, 6]]
        if not correct_input(a, b):  # Dimension test 2
            raise Exception("Dimension test 2 test failed")

        a = [[2, 4, 2], [5, 7, 5, 6, 64, 3]]
        b = [[5, 6], [7, 8], [12, 14]]
        if not correct_input(a, b):  # Differente sized rows test
            raise Exception("Differente sized rows test failed")

        print("~~~~~~~~~~~~~~ All Input tests passed ~~~~~~~~~~~~~~")
        return 1

    except Exception as out:
        print(out)
        return 0


if __name__ == "__main__":
    testing_input()
