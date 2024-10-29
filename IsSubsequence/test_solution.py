import solution as s

def test_on_subsequence():
    input_string = "ahbgdc"
    input_subsequence = "abc"
    except_result = True
    sol = s.Solution()
    result = sol.isSubsequence(input_subsequence, input_string)
    assert except_result == result

def test_on_constant_string():
    input_string = "bbaaaa"
    input_subsequence = "aaaaaa"
    except_result = False
    sol = s.Solution()
    result = sol.isSubsequence(input_subsequence, input_string)
    assert except_result == result


def test_on_not_subsequence():
    input_string = "parasolka"
    input_subsequence = "oal"
    except_result = False
    sol = s.Solution()
    result = sol.isSubsequence(input_subsequence, input_string)
    assert except_result == result

def test_reverse_order():
    input_string = "abddef"
    input_subsequence = "bdfe"
    except_result = False
    sol = s.Solution()
    result = sol.isSubsequence(input_subsequence, input_string)
    assert except_result == result