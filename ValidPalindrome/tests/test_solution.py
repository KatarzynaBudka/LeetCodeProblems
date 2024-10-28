import solution as s

def test_on_palindrome():
    input_string = "A man, a plan, a canal: Panama"
    except_result = True
    sol = s.Solution()
    result = sol.isPalindrome(input_string)
    assert except_result == result

def test_on_non_palindorme():
    input_string = "race a car"
    except_result = False
    sol = s.Solution()
    result = sol.isPalindrome(input_string)
    assert except_result == result

def test_on_empty_string():
    input_string = " "
    except_result = True
    sol = s.Solution()
    result = sol.isPalindrome(input_string)
    assert except_result == result

def test_on_string_with_number():
    input_string = "0P"
    except_result = False
    sol = s.Solution()
    result = sol.isPalindrome(input_string)
    assert except_result == result