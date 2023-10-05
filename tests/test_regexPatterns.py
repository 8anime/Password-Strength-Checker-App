
import pytest

from passwordChecker.regexPatterns import isValidPassword

# Test if isValidPassword correctly identifies a valid password.
def testValidPassword():
    assert isValidPassword('StrongP@ssword1') == True
    assert isValidPassword('AnotherV@lid2')  == True

# Test if isValidPassword correctly identifies an invalid password.
def testInvalidPassword():
    assert isValidPassword('short') == False                       # Passwords less than 8 characters
    assert isValidPassword('nouppercase123.')  == False            # Passwords that lack uppercase characters
    assert isValidPassword('NOLOWERCASE1/')  == False              # Passwords that lack lowercase characters
    assert isValidPassword('NOdigitInp@ssword') == False           # Passwords that lack digit characters
    assert isValidPassword('John@example.com')  == False           # Passwords that use email pattern
    assert isValidPassword('@username')  == False                  # Passowrds that use social media handles
    assert isValidPassword('2D4RN5D1X7R123456') == False           # Passwords that use matching vehicle indentification number
    assert isValidPassword('fe80::a6db:30ff:fe48:88de')  == False  # Passwords that use IPv6 Addresses pattern
    assert isValidPassword('Space in p@ssword2')  == False         # Passwords that allow spaces in between their characters
    assert isValidPassword('NoSpecial123')  == False               # Passwords that lack special case characters
    assert isValidPassword('Reeeeepetitive23./') == False          # Passwords with repetitive characters






















