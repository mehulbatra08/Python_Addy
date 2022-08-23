'''Write a program to calculate the grade of a student from his marks from the following scheme:
        90 - 100 (Excellent)
        80 -90    a
        70-80     b
        60-70     c
        50-60     d'''

marks = int(input("Enter your marks\n"))

if marks>90:
  grade = "Ex"
elif marks>=80:
    grade = "a"
elif marks>=70:
    grade = "b"
elif marks>=60:
    grade = "c"
elif marks>=50:
    grade = "d"
else:
    grade = "F"
print("Your grade is " + grade)