import random

choices = ['Rock', 'Paper', 'Scissor']
iterations = 3

points_fr_me = 0
points_fr_user = 0


def determine_winner(user_input, computer_input):
    global points_fr_me, points_fr_user

    if user_input == computer_input:
        print("It's a draw!")
    elif user_input == 'Rock' and computer_input == 'Paper':
        print("I win! Paper covers Rock.")
        points_fr_user += 1
    elif user_input == 'Rock' and computer_input == 'Scissor':
        print("You win! Rock crushes Scissors.")
        points_fr_me += 1
    elif user_input == 'Paper' and computer_input == 'Rock':
        print("You win! Paper covers Rock.")
        points_fr_me += 1
    elif user_input == 'Paper' and computer_input == 'Scissor':
        print("I win! Scissors cut Paper.")
        points_fr_user += 1
    elif user_input == 'Scissor' and computer_input == 'Rock':
        print("I win! Rock crushes Scissors.")
        points_fr_user += 1
    elif user_input == 'Scissor' and computer_input == 'Paper':
        print("You win! Scissors cut Paper.")
        points_fr_me += 1


def get_user_choice():
    for _ in range(iterations):
        user_choice = input("Enter your choice (Rock, Paper, or Scissor): ")
        computer_choice = random.choice(choices)

        print(f'Your choice: {user_choice}')
        print(f'My choice: {my_choice}')

        # Check if the user input is valid
        if user_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # Call the results function to determine the winner
        determine_winner(user_choice, my_choice)

    # Display final points after all iterations
    print(f"\nFinal Points - You: {points_fr_me}, Computer: {points_fr_user}")

