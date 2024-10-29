import solution as s

def test_on_simple_array():
    input_list = [2,3,1,2,4,3]
    target = 7
    expected_result = 2
    sol = s.Solution()
    result = sol.minSubArrayLen(target, input_list)
    assert result == expected_result

def test_on_array_without_sub_array():
    input_list = [1,1,1,2,1,3]
    target = 11
    expected_result = 0
    sol = s.Solution()
    result = sol.minSubArrayLen(target, input_list)
    assert result == expected_result
    
def test_on_two_solutions():
    input_list = [1,1,1,1,4]
    target = 4
    expected_result = 1
    sol = s.Solution()
    result = sol.minSubArrayLen(target, input_list)
    assert result == expected_result
