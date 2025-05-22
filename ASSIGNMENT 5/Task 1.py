# Module 6: Data Structures and Strings in Python

student = {}

def store_data():
    name = input("Enter the student's name: ")
    marks = int(input(name + "'s marks:"))
    student[name] = marks


def retrieve_marks():
    name = input("Enter the student's name: ")
    if name in student:
        print("Marks obtained: %d" % (student[name],))
    else:
        print("Student not found.")


store_data()
retrieve_marks()
