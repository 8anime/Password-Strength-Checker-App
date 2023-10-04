
import re

def isValidPassword(password):
    """This method checks if a password is valid by making sure that it is 
    at least 8 characters long, contains both upper and lower case letters
    and has at least 1 digit"""

    # Define a list of common patterns to disallow from passwords
    commonPatterns = [
        r'^(?:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$',  # Matches email-like patterns
        r'^(?:[A-HJ-NPR-Z0-9]{17})$',  # Matching Vehicle Identification Numbers (VIN)
        r'^(?:@[\w\d]+)$',  #  Matching Social Media Handles (e.g., @username)
        r'^(?:[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){7})$'  # Matching IPv6 Addresses
    ]

    pattern = rf'''
    (?=.*[A-Z])             # Must contain uppercase letters
    (?=.*[a-z])             # Must contain lowercase letters
    (?=.*\d)                # Must contain at least one digit
    (?=.*[\W_])             # Must contain at least one special character
    (?!.*\s)                # Must not contain space characters
    (?!.*(?:{'|'.join(commonPatterns)}))  # Must not contain common patterns or names
    (?!.*(\w)\1{{2,}})                    # Must not contain repetitive sequences of 3 or more characters
    .{{8,}}                               # Must be at least 8 characters long
    '''

    return bool(re.match(pattern, password, re.VERBOSE))  # 're.VERBOSE' enables whitespace and comments within the pattern for better readability
        








