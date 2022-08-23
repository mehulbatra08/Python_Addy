from email import message


def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return(f"Hi {name}")

message = get_greeting("Mehul")

print(message)

