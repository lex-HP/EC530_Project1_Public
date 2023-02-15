import Input_UnitTest
import Logic_UnitTest


def test_Input_and_Logic():
    Input_UnitTest.set_func2call(1)
    Input_result = Input_UnitTest.testing_input()
    Logic_UnitTest.set_func2call(1)
    Logic_result = Logic_UnitTest.testing_logic()

    if Input_result == 1 and Logic_result == 1:
        assert True
    elif Input_result == 0 and Logic_result == 1:
        assert False, "Input tests failed, Logic test passed"
    elif Input_result == 1 and Logic_result == 0:
        assert False, "Input tests passed, Logic test failed"
    elif Input_result == 0 and Logic_result == 0:
        assert False, "Input tests and Logic test failed"


if __name__ == "__main__":
    test_Input_and_Logic()
