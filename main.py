import format_details
from Student import Student
import connect_mongo as cm


while True:
    first_name = format_details.format_name(input("Enter your first name: ").strip())
    if first_name == "Invalid name":
        print("Invalid characters in input. Please enter a valid name.")
        continue
    else:
        while True:
            last_name = format_details.format_name(input("Enter your last name: ").strip())
            if last_name == "Invalid name":
                print("Invalid characters in input. Please enter a valid name.")
                continue
            else:
                full_name = first_name + " " + last_name
                print(f"Hello, {full_name}!")
                break
        break

while True:
    try:
        user_age = int(input("Enter your age: ").strip())
        if(format_details.format_age(user_age)):
            print(f"Your age is {user_age}.")
            break
        else:
            print("Invalid age. Please enter a valid age")
            continue
    except ValueError as err:
        print("Invalid characters in input. Please enter a valid age." + str(err))
        continue
    
subjects = {'physics': 0, 'chemistry': 0, 'biology': 0, 'maths': 0, 'english': 0}
for subject in subjects:
    while True:
        try:
            marks = int(input(f"Enter your marks in {subject}: ").strip())
            if(format_details.format_marks(marks)):
                subjects[subject] = marks
                break
            else:
                print("Invalid marks. Please enter valid marks")
                continue
        except ValueError as err:
            print("Invalid characters in input. Please enter valid marks." + str(err))
            continue
print("Your marks are:" + str(subjects))

student_bio = input("Enter your bio: ").strip()
file_name = (full_name + "_bio")
with open(file_name + ".txt", "w") as file:
    file.write(student_bio)
print(f"Your bio has been saved in {file_name}.txt")

courses = ["IT", "CS", "ME","EE"]
while True:

    print("Available courses are:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course}")
    try:
        course_choice = int(input("Enter the number of the course you want to choose: ").strip())
        if 1 <= course_choice <= len(courses):
            print(f"You have chosen {courses[course_choice - 1]} course.")
            course_choice = courses[course_choice - 1]
            print(f"Your course is {course_choice}")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            continue
    except ValueError as err:
        print("Invalid characters in input. Please enter a valid number." + str(err))
        continue

student_gender_options = ["M","F"]
while True:
    print("Please select your gender")
    for i, student_gender in enumerate (student_gender_options):
        print(f"{i + 1}. {student_gender}")
    try:
        student_gender = int(input("Select Gender: ").strip())
        if 1 <= student_gender <= len(student_gender_options):
            print(f"You have selected {student_gender_options[student_gender - 1]} gender")
            GENDER_OF_STUDENT = student_gender_options[student_gender - 1]
            print(f"You are {GENDER_OF_STUDENT}")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            continue
    except ValueError as err:
        print("Invalid characters in input. Please enter a valid number." + str(err))
        continue


student_1 = Student(first_name,
                    last_name,
                    full_name,
                    user_age,
                    subjects,
                    course_choice,
                    GENDER_OF_STUDENT,
                    student_bio
            )

for k, v in vars(student_1).items():
    print(k, v)

student_1_serialized = student_1.__dict__


cm.check_if_db_exist()
cm.check_if_collection_exist()
cm.insert_student_details(student_1_serialized)
cm.close_connection()