
import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

from regexPatterns import isValidPassword


class PasswordCheckerApp(QWidget):
    """The PasswordCheckerApp class is the main component of our PyQt5 application. It serves as the graphical 
    user interface (GUI) for checking the validity of passwords. This class is responsible for creating and managing 
    the application window, including widgets such as labels, input fields, and buttons. Users can input a password, click
    the 'Check Password' button, and receive immediate feedback on whether the password meets the required criteria for strength 
    and security. The class encapsulates the visual elements and functionality needed to assess password validity and provide a user-friendly 
    interface for this purpose."""
    def __init__(self):
        super().__init__()

        self.InitializeUserInterface()

    def InitializeUserInterface(self):
        """This method is used to build the user interface of the application"""
        self.setWindowTitle('Password Checker')  # Set the title for the application window
        self.setGeometry(450, 100, 400, 200)  # Set where on the screen the application will appear also it's width and height
        
        # Determines the arrangement and alignment of the various widgets within the application's main window
        # It is responsible for organizing the widgets in the main window in a vertical orientation from top to bottom
        widgetLayout = QVBoxLayout()

        self.passwordLabel = QLabel('Enter Password: ')  # Label asking for the password input
        self.passwordInput = QLineEdit()  # This is the field where the password will be inputed
        self.passwordInput.setPlaceholderText('Password must contain at least one special character (!@#$%^&*_).')
        # "The 'Check Password' button is used to verify if the entered password meets the specified criteria for a valid password
        self.checkPasswordButton = QPushButton('Check Password')

        self.strengthLabel = QLabel('Password Strength: ')

        # This label is used to give feedback to the user, whether the password is valid or NOT valid
        self.resultLabel = QLabel('')  

        widgetLayout.addWidget(self.passwordLabel)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.passwordInput)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.checkPasswordButton)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.resultLabel)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.strengthLabel)  # Add widget to the vertical orientation

        # Connect the button to a method that will analyze the password and check it's validity
        self.checkPasswordButton.clicked.connect(self.checkPassword)  

        self.setLayout(widgetLayout)  # Specify how the widgets should be arranged in the container widget(QWidget)

    def checkPassword(self):
        """This method is used to check if the password entered in the input box
        meets the criteria of a valid password or not"""
        tickImage = os.path.join('icons', 'tick.png')  # Construct a path to the tick.png file
        crossImage = os.path.join('icons', 'cross.png')  # Construct a path to the cross.png file

        password = self.passwordInput.text()  # Extract a text from the input box
        isValid = isValidPassword(password)  # Using the isValidPassword function, check if the password is valid
        if isValid:
            self.resultLabel.setPixmap(QPixmap(tickImage))  # If True using the QPixmap class, set the tick image
        else:
            self.resultLabel.setPixmap(QPixmap(crossImage)) # If False using the QPixmap class, set the cross image

        passwordStrength = self.calculatePasswordStrength(password)  # Return integer value from the calculatePasswordStrength method
        # Display feedback to the user about the strength of the password in form of percentage
        self.strengthLabel.setText(f'Password Strength: {passwordStrength}%')  

    def calculatePasswordStrength(self, password):
        """This method is used to calculate the password strength of a password"""
        # Initialize a base score
        score = 0
        
        # Check the number of characters in the password
        length = len(password)
        if length >= 8:
            score += 20  # Award 20% for a password of 8 characters or more
        else:
            return 0  # Password is too short, return 0% strength
    
        # Check for special characters
        specialCharacters = "!@#$%^&*()_+-=[]{}|;':,.<>?/~`"
        # Count the occurrences of characters in the password string that are also present in the specialCharacters string. 
        # It yields 2 for every character found, and when you sum these 2 values using the sum function, you get the count 
        # of special characters in the password string.
        numSpecialChars = sum(2 for char in password if char in specialCharacters)
        
        # Adjust the score based on the number of special characters
        score += numSpecialChars * 10  # Award 10% for each special character

        # Calculate the final score
        finalScore = min(score, 100)  # The score value should not exceed 100
    
        return finalScore  # Cap the score at 100%

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PasswordCheckerApp()
    window.show()

    sys.exit(app.exec_())



