import random

options = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    print(f"Computer: {computer_choice}")
    print(f"You: {user_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
        break
