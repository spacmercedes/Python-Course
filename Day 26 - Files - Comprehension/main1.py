numbers = range(1,5)
new_numbers = [n+1 for n in numbers]
print(new_numbers)

# names = ["ionel", "eva", "vasilica", "gheorghita", "viorel"]
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)
import random
names = ["ionel", "eva", "vasilica", "gheorghita", "viorel"]
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >50}
print(passed_students)