'''The game() funtion in a program lets a user play  game and returns the score as an integer
.You need to read a file 'hiscore.txt' which is either blank or contains the previous hiscore.
you need to write a program to update the hiscore whenever game() breaks the hi score'''


def game():
    return 44677
score=game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr=='':
    with open("hiscore.txt","w") as f:
        f.write(str(score))
elif int(hiScoreStr)<score:
    with open("hiScore.txt", "w") as f:
        f.writ(str(score))
