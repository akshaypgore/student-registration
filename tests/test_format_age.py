import sys
sys.path.append("../student_info")


from format_details import format_age

def test_format_age():

    # Test with a valid age
    assert format_age(20) == True

    # Test with an invalid age (negative)
    assert format_age(-5) == False

    # Test with an invalid age (under 18)
    assert format_age(10) == False

    # Test with an invalid age (exactly 0)
    assert format_age(0) == False

    # Test with an invalid age (exactly 18)
    assert format_age(18) == False
    