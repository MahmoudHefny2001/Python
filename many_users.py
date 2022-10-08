users = {

    'aeinstein': {
        'firstname': 'albert',
        'lastname': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'firstname': 'marie',
        'lastname': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['firstname']} {user_info['lastname']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


