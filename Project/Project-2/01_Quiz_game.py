# Create a Quizz game in which we will be asking the user 5 Questions if the user answer 4 out of 5 correct then we will print
# Hey! you got 4 out of 5.



from image import quiz_time
print(quiz_time)
print("Hey! Welcome to the Quiz Game! We are Going to ask you 5 Questions and you are supposed to answer them all! ")
name = input("Enter your name\n")

answer_list = []

ques1 = input("Is 51 a Prime Number?Type 'yes' or 'no' \n")
if ques1 == 'yes':
    print("You got it right")
    answer_list.append("1")
elif ques1 == 'no':
    print("Sorry! Wrong answer!")


ques2 = input("Do camels have three sets of eyelids?Type 'yes' or 'no'\n")
if ques2 == 'yes':
    print("You got it right")
    answer_list.append("1")
elif ques2 == 'no':
    print("Sorry! Wrong answer!")


ques3 = input("There is no railway system in Iceland.Type 'yes' or 'no'\n")
if ques3 == 'yes':
    print("You got it right")
    answer_list.append("1")
elif ques3 == 'no':
    print("Sorry! Wrong answer!")


ques4 = input("Is it possible to sneeze during sleeping ?Type 'yes' or 'no' \n")
if ques4 == 'yes':
    print("Sorry! Wrong answer!")
elif ques4 == 'no':
    print("You got it right")
    answer_list.append("1")

ques5 = input("Canada is the Third Largest country in the world.Type 'yes' or 'no' \n")
if ques5 == 'yes':
    print("Sorry! Wrong answer!")
elif ques5 == 'no':
    print("You got it right")
    answer_list.append("1")


user_score = len(answer_list)

Total_score = 5

print(f"{name} scored {user_score} out of {Total_score}")



