import random

# Define the choices
choices = ['rock', 'paper', 'scissors']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

# Function to update the score
def update_score(result, scores):
    if result == 'You win!':
        scores['user'] += 1
    elif result == 'You lose!':
        scores['computer'] += 1
    else:
        scores['tie'] += 1

# Game loop
# Initialize scores
scores = {'user': 0, 'computer': 0, 'tie': 0}

play_again = True
while play_again:
    # Get the user's choice
    user_choice = input('Enter your choice (rock, paper, or scissors): ').lower()
    # Validate the user's choice
    while user_choice not in choices:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        user_choice = input('Enter your choice (rock, paper, or scissors): ').lower()

    # Get the computer's choice
    computer_choice = random.choice(choices)

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print('The computer chose:', computer_choice)

    # Call the function to update the score
    update_score(result, scores)
    print('Score:')
    print('User:', scores['user'])
    print('Computer:', scores['computer'])
    print('Tie:', scores['tie'])

    # Ask if the user wants to play again
    play_again_input = input('Do you want to play again? (y/n): ').lower()
    play_again = play_again_input == 'y'

    # Check if the user wants to display the score
    if play_again_input == 'n':
        print('Final Score:')
        print('User:', scores['user'])
        print('Computer:', scores['computer'])
        print('Tie:', scores['tie'])
    
