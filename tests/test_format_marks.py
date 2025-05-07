import sys
sys.path.append("../student-registration")

from format_details import format_marks

def test_format_marks():
    # Test with valid marks
    assert format_marks(50) == True

    # Test with invalid marks
    assert format_marks(-1) == False
    assert format_marks(101) == False
    assert format_marks(0) == True
    assert format_marks(100) == True