import sys
sys.path.append("../student_info")

from format_details import format_name

def test_format_name():

    # Test with a valid name
    assert format_name("akshAy") == "Akshay"

    # Test with an invalid name
    assert format_name("aksha@y") == "Invalid name"
    