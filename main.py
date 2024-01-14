import sys
import random
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

images = ['images/fist.png',
          'images/palm-of-hand.png',
          'images/scissor.png',
          'images/blank.png']

choices = ['Rock', 'Paper', 'Scissor']

points_fr_me = 0
points_fr_user = 0

exit_flag = False


def determine_winner(user_input, computer_input):
    global points_fr_me, points_fr_user
    comment = ''

    if user_input == computer_input:
        comment = "It's a draw!"
    elif user_input == 'Rock' and computer_input == 'Paper':
        comment = "I win! Paper covers Rock."
        points_fr_user += 1
    elif user_input == 'Rock' and computer_input == 'Scissor':
        comment = "You win! Rock crushes Scissors."
        points_fr_me += 1
    elif user_input == 'Paper' and computer_input == 'Rock':
        comment = "You win! Paper covers Rock."
        points_fr_me += 1
    elif user_input == 'Paper' and computer_input == 'Scissor':
        comment = "I win! Scissors cut Paper."
        points_fr_user += 1
    elif user_input == 'Scissor' and computer_input == 'Rock':
        comment = "I win! Rock crushes Scissors."
        points_fr_user += 1
    elif user_input == 'Scissor' and computer_input == 'Paper':
        comment = "You win! Scissors cut Paper."
        points_fr_me += 1

    return comment


def gotoHome():
    home = HomeScreen()
    widget.addWidget(home)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def gotoResults():
    results = ResultScreen()
    widget.addWidget(results)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("Start-game.ui", self)
        self.Start_Button.clicked.connect(gotoHome)


class HomeScreen(QMainWindow):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("game.ui", self)

        self.text = None
        self.Command = None
        self.click_count = 1
        self.user_input = ''

        self.Button_R.clicked.connect(self.show_rock)
        self.Button_P.clicked.connect(self.show_paper)
        self.Button_S.clicked.connect(self.show_scissor)
        self.Exit_Button.clicked.connect(self.delayed_goto_results)

    def reset_all(self):
        self.User_input_img.setPixmap(QPixmap(images[3]))
        self.Com_input_img.setPixmap(QPixmap(images[3]))
        self.Command.setText('Your turn')

    def show_rock(self):
        self.update_ui()
        self.play_game()
        self.user_input = 'Rock'
        print(self.user_input)
        self.User_input_img.setPixmap(QPixmap(images[0]))

    def show_paper(self):
        self.update_ui()
        self.play_game()
        self.user_input = 'Paper'
        print(self.user_input)
        self.User_input_img.setPixmap(QPixmap(images[1]))

    def show_scissor(self):
        self.update_ui()
        self.play_game()
        self.user_input = 'Scissor'
        print(self.user_input)
        self.User_input_img.setPixmap(QPixmap(images[2]))

    def play_game(self):
        computer_input = random.choice(choices)
        result = determine_winner(self.user_input, computer_input)
        print(computer_input)

        if computer_input == 'Rock':
            self.Com_input_img.setPixmap(QPixmap(images[0]))
        elif computer_input == 'Paper':
            self.Com_input_img.setPixmap(QPixmap(images[1]))
        elif computer_input == 'Scissor':
            self.Com_input_img.setPixmap(QPixmap(images[2]))

        #print(result)

    def update_ui(self):
        global exit_flag

        self.click_count += 1
        print(f"Click count: {self.click_count}")
        self.text = f'Round: {self.click_count}'

        if self.click_count != 4:
            self.Round.setText(self.text)
            QTimer.singleShot(1000, lambda: self.reset_all)
        else:
            exit_flag = True
            QTimer.singleShot(500, self.delayed_goto_results)

        print(self.user_input)

    def delayed_goto_results(self):
        print("game over")
        if exit_flag:
            gotoResults()


class ResultScreen(QMainWindow):
    def __init__(self):
        super(ResultScreen, self).__init__()
        loadUi("Stop-game.ui", self)
        self.Again_Button.clicked.connect(gotoHome)


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
