# Write a python Program where you input marks of some students as a list and you need to find the maximum marks out of them using for loop

student_marks = input("Enter the student marks in series\n").split()

#We need to convert the elements in list into strings
for n in range(0,len(student_marks)):
    student_marks[n] = int(student_marks[n])



print(student_marks)


highest_marks = 0
for marks in student_marks:
    if marks > highest_marks:
        highest_marks = marks
print(highest_marks)