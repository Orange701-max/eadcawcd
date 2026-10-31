student_profile = ("Aarav", "Grade 6", "Section A", 6)
student_name = student_profile[0]
student_grade = student_profile[1]
student_section = student_profile[2]
student_age = student_profile[3]
print("Student Name:", student_name)
print("Student Grade:", student_grade)
print("Student Section:", student_section)
print("Student Age:", student_age)
print("First two details:", student_profile[0:2])

monday_subjects = {"Math", "Science", "English", "Computer", "Art"}
tuesday_subjects = {"Math", "History", "English", "Sports", "Music"}
print("\nMonday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
monday_subjects.add("Library")
monday_subjects.discard("Art")
tuesday_subjects.add("Drama")
tuesday_subjects.discard("Sports")
print("\nUpdated Monday Subjects:", monday_subjects)
print("Updated Tuesday Subjects:", tuesday_subjects)

all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
print("\nAll Subjects:", all_subjects)
print("Common Subjects:", common_subjects)