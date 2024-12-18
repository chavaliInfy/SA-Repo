 # Check the length of the password
    if len(password) < min_length:
        print("Password is too short!")
        return False

    # Check if the password contains an uppercase letter, lowercase letter, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    # Print an error message for each missing criteria
    if not has_uppercase:
        print("Password must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one digit!")
        return False
    if not has_special_char:
        print("Password must contain at least one special character!")
        return False

    # If all criteria are met, print a success message
    print("Password is strong!")
    return True

# Prompt the user to enter a password and check if it meets the criteria
password = input("Enter a password: ")
password_checker(password)
