import pytest
import solution as s

def test_on_simple_string():
    input_string = 'Hello World'
    except_result = 5
    sol = s.Solution()
    result = sol.lengthOfLastWord(input_string)
    assert result == except_result

def test_on_multiple_spaces():
    input_string = '   fly me   to   the moon  '
    except_result = 4
    sol = s.Solution()
    result = sol.lengthOfLastWord(input_string)
    assert result == except_result

def test_on_single_character():
    input_string = 't'
    except_result = 1
    sol = s.Solution()
    result = sol.lengthOfLastWord(input_string)
    assert result == except_result

