
# Password Strength Checker

## Overview

The Password Strength Checker is a Python application built using PyQt5 that allows users to assess the strength and security of their passwords. It provides immediate feedback on whether a password meets certain criteria for strength.

## Features

- Checks password length: Passwords must be at least 8 characters long.
- Requires a mix of uppercase and lowercase letters.
- Requires at least one digit.
- Requires at least one special character from the following: !@#$%^&*.
- Does not allow spaces between characters.
- Avoids common patterns, such as email-like patterns, Vehicle Identification Numbers (VIN), social media handles, and IPv6 Addresses.
- Prevents repetitive sequences of 3 or more characters.

## Usage

### Installation

1. Clone the repository to your local machine: git clone https://github.com/8anime/Password-Strength-Checker-App.git

2. Install the required libraries using pip

### Running the Application

1. Execute the `passwordStrengthChecker.py` script to start the Password Strength Checker application.

### User Interface

The application's user interface consists of the following components:

- **Password Input Field**: Enter the password you want to check.
- **Check Password Button**: Click this button to analyze the entered password.
- **Result Label**: This label provides immediate feedback on whether the password is valid or not, along with a graphical indicator.

### Checking Password Strength

After entering your password and clicking the "Check Password" button, the application will analyze the password based on the criteria mentioned above.

### Feedback

You will receive visual feedback in the form of a checkmark or cross icon, indicating whether the password is valid or not.

## Testing

The application includes a set of unit tests to verify its functionality. You can run the tests using the `pytest` command. The tests are located in the `tests` directory.

License
This project is licensed under the MIT License - see the LICENSE file for details.

