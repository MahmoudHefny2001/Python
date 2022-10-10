def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

usernames = ['mahmoud', 'aly', 'mostafa', 'mohammed', 'alaa', 'hany', 'khaled']
greet_users(usernames)
