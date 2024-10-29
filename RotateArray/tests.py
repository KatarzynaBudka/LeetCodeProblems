import pytest
import solution as s

def test_on_simple_list():
    input_list = [1,2,3,4,5,6,7]
    input_k = 3
    except_result = [5,6,7,1,2,3,4]
    sol = s.Solution()
    result = sol.rotate(input_list, input_k)
    assert result == except_result

def test_on_simple_list_second():
    input_list = [-1,-100,3,99]
    input_k = 3
    except_result = [3,99, -1, -100]
    sol = s.Solution()
    result = sol.rotate(input_list, input_k)
    assert result == except_result

def test_on_k_bigger_than_lenght():
    input_list = [1,2,3]
    input_k = 5
    except_result = [2,3,1]
    sol = s.Solution()
    result = sol.rotate(input_list, input_k)
    assert result == except_result

def test_on_one_element_list():
    input_list = [1]
    input_k = 3
    except_result = [1]
    sol = s.Solution()
    result = sol.rotate(input_list, input_k)
    assert result == except_result