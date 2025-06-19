# courselist2.py - Adding courses more efficiently
# Matthew Raines, COP2500

# This code was written to help register and organize courses for the Knightrola
# region's students.

# format_input: Given a list of strings, capitalizes and strips extra spaces for
# each item in the list. Returns the formatted list. Causes an error if the
# list isn't made up of strings.

def format_input(string_list):
    for i, s in enumerate(string_list):
        string_list[i] = s.title().strip()

    return string_list

# add_courses: Given the course list, asks the user what courses they want to
# add, turns it into a list, and formats the list. It then adds the courses
# to the course list. Returns the list. Causes an error if it's not given a list.

def add_courses(course_list):
    course_add_list = input("\nEnter courses to add: ")

    course_add_list = course_add_list.split(",") 
    course_add_list = format_input(course_add_list)

    course_list += course_add_list
    course_number_display(course_list)
    return course_list

# remove_courses: Given the course list, asks the user which courses they want
# to remove, turns it into a list, and formats the list. It then removes those
# courses from the course list. Causes an error if it's not given a list.

def remove_courses(course_list):
    course_remove_list=input("\nEnter the courses you'd like to drop: ")
    course_remove_list=course_remove_list.split(",")
    format_input(course_remove_list)

    for s in course_remove_list:
        if s in course_list:
            course_list.remove(s)
    course_number_display(course_list)
    return course_list

# course_number_display: Displays each course given the course list. Returns
# nothing. Causes an error if it's not given a list.

def course_number_display(course_list):
    print("\nCurrent course List:")
    for i in range(len(course_list)):
        print(i+1,". ",course_list[i],sep="")

# --- MAIN PROGRAM ---

# Sets up empty list

course_list = []

# Sets up a loop to prompt courses to be added if there's less than 5 or to be
# removed if there's more than 5. Ends when there's 5 courses.

while len(course_list) != 5:
    if len(course_list) < 5:
        course_list = add_courses(course_list)
        
    elif len(course_list) > 5:
        course_list = remove_courses(course_list)

print("\nAll done!")
