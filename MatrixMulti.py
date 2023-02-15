# numpyless matrix multiplication with error handling
# does not take in numpy arrays or complex numbers


def matrix_multiplication(Mat_A, Mat_B):
    input_check = input_error_check(Mat_A, Mat_B)
    if input_check == 1:
        result = matmul(Mat_A, Mat_B)
        return result
    else:
        return input_check


# This is the function for doing Matrix Multiplication without using numpy
def matmul(Mat_A, Mat_B):

    row_size_A = len(Mat_A)
    row_size_B = len(Mat_B)
    col_size_B = len(Mat_B[0])
    # Math
    # initialise ouput matrix
    out = [[0]*col_size_B for m in range(row_size_A)]
    for i in range(row_size_A):
        for j in range(col_size_B):
            for k in range(row_size_B):
                out[i][j] = out[i][j] + Mat_A[i][k] * Mat_B[k][j]
    return out

# This is the module for checking if inputs are in correct format


def input_error_check(Mat_A, Mat_B):
    # in numpyless python, matrices are lists of lists
    try:
        if (type(Mat_A) != list) or (type(Mat_B) != list):
            raise Exception("Wrong input type")  # check if they are a list

        for Mat in (Mat_A, Mat_B):
            uniformity_check = 0
            for row in Mat:
                if type(row) != list:
                    # check if they are a list of list
                    raise Exception("Wrong input type")

                for item in row:
                    if isinstance(item, (int, float)) == 0:
                        # check if they are a list of list of numerical values
                        raise Exception("Item type not supported")

                # second statement is here to diseable the check on first loop
                if (uniformity_check != len(row)) and row != Mat[0]:
                    # check if all the lists are of equal size
                    raise Exception("Rows are not of equal size")
                uniformity_check = len(row)

        col_size_A = len(Mat_A[0])
        row_size_B = len(Mat_B)
        if (col_size_A != row_size_B):
            # Check if input dimensions are matrix multiplication friendly
            raise Exception("Column size of A needs to be equal to row size B")

        return 1

    except Exception as result:
        return result


if __name__ == '__main__':
    a = [[2, '5', 2], [5, 7, 5]]
    b = [[5, 6], [7, 8], [-12, 14.65]]
    # out = input_error_check(a, b)
    # out = matmul(a,b)
    out = matrix_multiplication(a, b)
    print(out)
