#def greet_user():
   # """Dispaly a simple greeting"""
   # print("Hello!")

#greet_user()


#def greet_user(username):
   # """Display a simple greeting."""
   # print(f"Hello, {username.title()}!")

#name = input("Enter your name: ")
#greet_user(name)
#greet_user('Jesse')



def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!

while True:
    print("\nPlease tell me your name: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\nHello, {formatted_name}!")

    answer = input("If you wanna quit press q, to continue press any key: ")
    if answer.lower() == 'q':
        break
    else:
       continue



















