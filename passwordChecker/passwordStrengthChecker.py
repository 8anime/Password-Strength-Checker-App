
import sys

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
        # "The 'Check Password' button is used to verify if the entered password meets the specified criteria for a valid password
        self.checkPasswordButton = QPushButton('Check Password')

        # This label is used to give feedback to the user, whether the password is valid or NOT valid
        self.resultLabel = QLabel('Result: ')  

        widgetLayout.addWidget(self.passwordLabel)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.passwordInput)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.checkPasswordButton)  # Add widget to the vertical orientation
        widgetLayout.addWidget(self.resultLabel)  # Add widget to the vertical orientation

        # Connect the button to a method that will analyze the password and check it's validity
        self.checkPasswordButton.clicked.connect(self.checkPassword)  

        self.setLayout(widgetLayout)  # Specify how the widgets should be arranged in the container widget(QWidget)

    def checkPassword(self):
        """This method is used to check if the password entered in the input box
        meets the criteria of a valid password or not"""
        password = self.passwordInput.text()  # Extract a text from the input box
        isValid = isValidPassword(password)  # Using the isValidPassword function, check if the password is valid
        if isValid:
            self.resultLabel.setText('Result: Password is valid')  # If True set this text to the resultLabel widget
        else:
            self.resultLabel.setText('Result: Password is invalid')  # If False set this text to the resultLabel widget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PasswordCheckerApp()
    window.show()

    sys.exit(app.exec_())



