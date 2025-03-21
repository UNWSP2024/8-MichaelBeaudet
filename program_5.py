# Title: Program 5 Week 8
# Author: Michael Beaudet
# Date: 3/21/25

def main():
# Initialize an dictionary to store course ID and name pairs
    courses = {}
# Input course data
    while True:
        course_id = input("Enter course ID (or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input(f"Enter course name for {course_id}: ")
        courses[course_id] = course_name
# Get the subject to search for
    subject = input("Enter the subject to search for (e.g. 'COS'): ")
# Display courses with the matching subject
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")

if __name__ == "__main__":
    main()