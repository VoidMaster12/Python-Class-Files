# courselist.py - Lists of courses
# Matthew Raines, COP 2500

# This code was created to manage and organize course schedules.

# add_course: Given the course list and the desired course, adds the course to
# the list.  If there's 6 courses in the list, it prompts one to be removed.
# Returns the list. Causes an error if it's not given a list.

def add_course(course_list, course):
    course_list.append(course)
    if len(course_list) <= 5:
        course_number_display(course_list)
    else:
        print("You have more than five courses. You must drop one.")
        course_list = remove_course(course_list)
    return course_list

# remove_course: Given the course list, asks the user for the number of the
# course to be removed, and removes the course from the list. Causes an error if
# it's not given a list.

def remove_course(course_list):
    course_number_display(course_list)
    course_num = int(input("Enter the number besides the course you'd like to drop: "))
    course_list.pop(course_num - 1)
    course_number_display(course_list)
    return course_list

# course_number_display: Displays the number for each course given the course
# list. It then calls the function to assign course numbers. Returns nothing.
# Causes an error if it's not given a list.

def course_number_display(course_list):
    print("\nCourse List:")
    for i, course in enumerate(course_list):
        print(f"{i + 1}. {course}")

#---MAIN PROGRAM---

# Sets up empty list and course variable.
course_list = []

course = ""

# Creates a loop to ask the user to add a course as long as the user doesn't
# enter EXIT. It then adds the course using functions.

while course != "Exit":
    course = input("\nType EXIT to quit\n""Enter a course to add: ")
    course = course.upper().strip()
    if course == "Exit":
        course_number_display(course_list)
        break
    else:
        course_list = add_course(course_list,course)

# Prints that the user is finished, ends the program.

print("You are finished, thank you!")