import solution as s


def test_on_simple_list():
    input_list = [1,1,1,2,2,3]
    except_list = [1,1,2,2,3]
    except_result = 5
    sol = s.Solution()
    result = sol.removeDuplicates(input_list)
    assert except_list == input_list
    assert except_result == result

def test_on_correct_list():
    input_list = [1,1,2,2,3]
    except_list = [1,1,2,2,3]
    except_result = 5
    sol = s.Solution()
    result = sol.removeDuplicates(input_list)
    assert except_list == input_list
    assert except_result == result

def test_on_one_element_list():
    input_list = [1]
    except_list = [1]
    except_result = 1
    sol = s.Solution()
    result = sol.removeDuplicates(input_list)
    assert except_list == input_list
    assert except_result == result