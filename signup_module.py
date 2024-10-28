def signup_user(username, password, email):\n    if "@" not in email:\n        print("Invalid email address")\n        return False\n    print(f"Signing up user: {username}")\n    return True
