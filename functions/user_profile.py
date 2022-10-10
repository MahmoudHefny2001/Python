def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first_name.title()
    user_info['last_name'] = last_name.title()
    return user_info


user_profile = build_profile('mahmoud', 'hefny', location='Assiut', field='IT')

print(user_profile)
