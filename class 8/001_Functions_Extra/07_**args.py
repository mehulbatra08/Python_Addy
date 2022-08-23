from unicodedata import name
from matplotlib.colors import same_color


def save_user(**user):
    print(user)

save_user(id = 1,name="John",age = 22)

# {'id': 1, 'name': 'John', 'age': 22} --> Output
# They are in the form of a dictionary

