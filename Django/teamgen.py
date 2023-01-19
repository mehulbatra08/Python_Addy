import random
player_list = ["x", "y", "z", "a", "b", "c"]

# def choose():
#     y = random.choice(player_list)
#     return y
# team_formed = []

# for i in range(3):
#     k = choose()
#     if k in team_formed:        
#         choose()
#     else:
#         team_formed.append(y)

# print(team_formed)

# print(choose())
team_formed = []
def choose():
    y = random.choice(player_list)
    if y not in team_formed:
        team_formed.append(y)
    else:
        choose()
print(team_formed)




