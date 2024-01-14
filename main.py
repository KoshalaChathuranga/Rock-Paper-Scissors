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

points_fr_computer = 0
points_fr_user = 0

exit_flag = False


def determine_winner(user_input, computer_input):
    global points_fr_computer, points_fr_user
    comment = ''

    if user_input == computer_input:
        comment = "It's a draw!"
    elif user_input == 'Rock' and computer_input == 'Paper':
        comment = "I win! Paper covers Rock."
        points_fr_computer += 1
    elif user_input == 'Rock' and computer_input == 'Scissor':
        comment = "You win! Rock crushes Scissors."
        points_fr_user += 1
    elif user_input == 'Paper' and computer_input == 'Rock':
        comment = "You win! Paper covers Rock."
        points_fr_user += 1
    elif user_input == 'Paper' and computer_input == 'Scissor':
        comment = "I win! Scissors cut Paper."
        points_fr_computer += 1
    elif user_input == 'Scissor' and computer_input == 'Rock':
        comment = "I win! Rock crushes Scissors."
        points_fr_computer += 1
    elif user_input == 'Scissor' and computer_input == 'Paper':
        comment = "You win! Scissors cut Paper."
        points_fr_user += 1

    return comment, points_fr_computer, points_fr_user


def gotoHome():
    home = HomeScreen()
    widget.addWidget(home)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def gotoResults():
    results = ResultScreen()
    widget.addWidget(results)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    print(f'you: {points_fr_user} & computer: {points_fr_computer}')
    
 
    
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
        self.click_count = 0
        self.user_input = ''
        self.result = ''
        self.points_user = None
        self.points_computer = None
        
        self.Button_R.clicked.connect(self.show_rock)
        self.Button_P.clicked.connect(self.show_paper)
        self.Button_S.clicked.connect(self.show_scissor)
        self.Exit_Button.clicked.connect(self.delayed_goto_results)

    def show_rock(self):
        self.user_input = 'Rock'
        self.update_ui()
        self.play_game()
        self.User_input_img.setPixmap(QPixmap(images[0]))

    def show_paper(self):
        self.user_input = 'Paper'
        self.update_ui()
        self.play_game()
        self.User_input_img.setPixmap(QPixmap(images[1]))

    def show_scissor(self):
        self.user_input = 'Scissor'
        self.update_ui()
        self.play_game()
        self.User_input_img.setPixmap(QPixmap(images[2]))

    def play_game(self):
        computer_input = random.choice(choices)
        self.result, self.points_computer, self.points_user = determine_winner(self.user_input, computer_input)
        
        print(f'Your choice: {self.user_input}')
        print(f'My choice: {computer_input}')
        
        self.set_comments()

        if computer_input == 'Rock':
            self.Com_input_img.setPixmap(QPixmap(images[0]))
        elif computer_input == 'Paper':
            self.Com_input_img.setPixmap(QPixmap(images[1]))
        elif computer_input == 'Scissor':
            self.Com_input_img.setPixmap(QPixmap(images[2]))


    def update_ui(self):
        global exit_flag

        self.click_count += 1
        print(f"Click count: {self.click_count}")
        self.text = f'Round: {self.click_count}'

        if self.click_count != 3:
            self.Round.setText(self.text)
            QTimer.singleShot(1000, self.reset_all)
        else:
            exit_flag = True
            QTimer.singleShot(1000, self.delayed_goto_results)
            
    def reset_all(self):
        self.User_input_img.setPixmap(QPixmap(images[3]))
        self.Com_input_img.setPixmap(QPixmap(images[3]))
        self.comments.setText('Your turn')
        print('all reset')
    
    def set_comments(self):
        self.comments.setText(self.result)
        
    def delayed_goto_results(self):
        print("game over")
        if exit_flag:
            gotoResults()


class ResultScreen(QMainWindow):
    def __init__(self):
        super(ResultScreen, self).__init__()
        loadUi("Stop-game.ui", self)
        self.Again_Button.clicked.connect(gotoHome)
        self.display_results()
    
    def display_results(self):
        global points_fr_computer, points_fr_user
        
        if points_fr_computer == points_fr_user:
            self.results.setText('Its a draw')
            self.forComputer.setText(str(points_fr_computer))
            self.forUser.setText(str(points_fr_user))
        elif points_fr_computer > points_fr_user:
            self.results.setText('You Loss')
            self.forComputer.setText(str(points_fr_computer))
            self.forUser.setText(str(points_fr_user))
        elif points_fr_computer < points_fr_user:
            self.results.setText('You Won')
            self.forComputer.setText(str(points_fr_computer))
            self.forUser.setText(str(points_fr_user))
            
        points_fr_computer = 0
        points_fr_user = 0
    
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
