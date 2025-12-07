import csv
from logging import exception

from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    class that sets up the main window of the grading application
    """
    def __init__(self)->None:
        """
        method that sets up the main window of the grading application
        hides every label and entry line until called in later methods
        opens a file ready for input
        """
        super().__init__()
        self.setFixedSize(294, 351)
        self.setupUi(self)
        self.submitButton.clicked.connect(lambda: self.submit())
        self.submitButton_2.clicked.connect(lambda: self.submit())
        self.resetButton.clicked.connect(lambda: self.reset())
        self.submitButton_2.hide()

        self.scoreOneLabel.hide()
        self.scoreTwoLabel.hide()
        self.scoreThreeLabel.hide()
        self.scoreFourLabel.hide()

        self.scoreOneEntry.hide()
        self.scoreTwoEntry.hide()
        self.scoreThreeEntry.hide()
        self.scoreFourEntry.hide()

        self.attemptEntry.setPlaceholderText("Enter up to 4 attempts")

        f = open('grades.csv', 'w')
        writer = csv.writer(f)
        header = ['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final']
        writer.writerow(header)


    def submit(self)->None:
        """
        method to submit each student and their grade results
        throws exceptions if invalid input is entered
        :return:
        """
        self.submitButton.hide()
        self.submitButton_2.show()
        try:
            name = self.studentEntry.text()
            if name.isalpha():
                name = name
            else:
                raise ValueError
            attempts = int(self.attemptEntry.text())

        except:
            self.messageLabel.setStyleSheet("color: blue")
            self.messageLabel.setText('Enter valid name and number of attempts')

        else:

            try:
                if attempts == 1:
                        self.scoreOneLabel.show()
                        self.scoreOneEntry.show()
                        self.scoreTwoEntry.hide()
                        self.scoreTwoLabel.hide()
                        self.scoreThreeLabel.hide()
                        self.scoreThreeEntry.hide()
                        self.scoreFourLabel.hide()
                        self.scoreFourEntry.hide()
                        scoreOne_1 = int(self.scoreOneEntry.text())
                        scores =[scoreOne_1]
                        self.range(scores)
                        info = [name, scoreOne_1, '0', '0', '0', scoreOne_1]
                        self.file(info)



                elif attempts == 2:

                    self.scoreOneLabel.show()
                    self.scoreOneEntry.show()
                    self.scoreTwoLabel.show()
                    self.scoreTwoEntry.show()
                    self.scoreThreeLabel.hide()
                    self.scoreThreeEntry.hide()
                    self.scoreFourLabel.hide()
                    self.scoreFourEntry.hide()
                    scoreOne_2 = self.scoreOneEntry.text()
                    scoreTwo_2 = self.scoreTwoEntry.text()
                    scores = [scoreOne_2, scoreTwo_2]
                    self.range(scores)
                    info = [name, scoreOne_2, scoreTwo_2]
                    self.file(info)

                elif attempts == 3:

                    self.scoreOneLabel.show()
                    self.scoreOneEntry.show()
                    self.scoreTwoLabel.show()
                    self.scoreTwoEntry.show()
                    self.scoreThreeLabel.show()
                    self.scoreThreeEntry.show()
                    self.scoreFourLabel.hide()
                    self.scoreFourEntry.hide()


                    scoreOne_3 = int(self.scoreOneEntry.text())
                    scoreTwo_3 = int(self.scoreTwoEntry.text())
                    scoreThree_3 = int(self.scoreThreeEntry.text())

                    scores = [scoreOne_3, scoreTwo_3, scoreThree_3]
                    self.range(scores)
                    final = max(scores)
                    info = [name, scoreOne_3, scoreTwo_3, scoreThree_3, '0', final]
                    self.file(info)

                elif attempts == 4:
                    self.scoreOneLabel.show()
                    self.scoreOneEntry.show()
                    self.scoreTwoLabel.show()
                    self.scoreTwoEntry.show()
                    self.scoreThreeLabel.show()
                    self.scoreThreeEntry.show()
                    self.scoreFourLabel.show()
                    self.scoreFourEntry.show()

                    scoreOne_4 = int(self.scoreOneEntry.text())
                    scoreTwo_4 = int(self.scoreTwoEntry.text())
                    scoreThree_4 = int(self.scoreThreeEntry.text())
                    scoreFour_4 = int(self.scoreFourEntry.text())

                    scores = [scoreOne_4, scoreTwo_4, scoreThree_4, scoreFour_4]
                    self.range(scores)
                    final = max(scores)
                    info = [name, scoreOne_4, scoreTwo_4, scoreThree_4, scoreFour_4, final]
                    self.file(info)
            except:
                    self.messageLabel.setText('Scores must be numeric and within 0-99')

    def range(self, numbers)->None:
        """
        method to ensure that the grade entered is within the correct range
        :param numbers

        """
        for num in numbers:
            if not (0 <= num <= 100):
                raise IndexError(self.messageLabel.text('NUM MUST BE BETWEEN 0 and 100'))

    def file(self, info1)->None:
        """
        method to append the grading info to a csv file
        :param info1:
        :return:
        """
        with open('grades.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(info1)
            self.messageLabel.setStyleSheet('color: green')
            self.messageLabel.setText('Value stored!')



    def reset(self)->None:
        """
        method to reset the entire application and csv file in case of error when entering grades
        :return:
        """
        self.submitButton_2.hide()
        self.submitButton.show()
        self.studentEntry.clear()
        self.attemptEntry.clear()
        self.scoreOneLabel.hide()
        self.scoreOneEntry.hide()
        self.scoreOneEntry.clear()
        self.scoreTwoLabel.hide()
        self.scoreTwoEntry.hide()
        self.scoreTwoEntry.clear()
        self.scoreThreeLabel.hide()
        self.scoreThreeEntry.hide()
        self.scoreThreeEntry.clear()
        self.scoreFourLabel.hide()
        self.scoreFourEntry.hide()
        self.scoreFourEntry.clear()
        self.messageLabel.setText('')
        s = open('grades.csv', 'w')
        s.close()
        f = open('grades.csv', 'w')
        writer = csv.writer(f)
        header = ['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final']
        writer.writerow(header)










