
import re

def isValidPassword(password):
    """This method checks if a password is valid by making sure that it is 
    at least 8 characters long, contains both upper and lower case letters
    and has at least 1 digit"""
    pattern = r'''(
    (?=.*[A-Z])  # Must contain uppercase letters
    (?=.*[a-z])  # Must contain lowercase letters
    (?=.*\d)     # Must contain at least one digit
    .{8,}        # Must be at least 8 characters long
    )'''

    if re.match(pattern, password, re.VERBOSE):  # 're.VERBOSE' enables whitespace and comments within the pattern for better readability
        print('Password meets the criteria')
    else:
        print('Password does not meet the criteria')








