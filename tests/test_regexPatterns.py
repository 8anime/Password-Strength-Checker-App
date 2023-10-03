
import pytest

from passwordChecker.regexPatterns import isValidPassword

# Test if isValidPassword correctly identifies a valid password.
def testValidPassword():
    assert isValidPassword('Abcdefghi1') == True

# Test if isValidPassword correctly identifies an invalid password.
def testInvalidPassword():
    assert isValidPassword('abc123')  == False






















