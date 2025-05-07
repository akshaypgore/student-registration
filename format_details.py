def format_name(user_name: str) -> str:
    if user_name.isalpha():
        return user_name.capitalize()
    else:
        return "Invalid name"

def format_age(user_age: int) -> bool:
    if user_age <= 0  or 0 < user_age <= 18:
        return False
    else:
        return True

def format_marks(marks: int) -> bool:
    if marks < 0 or marks > 100:
        return False
    else:
        return True