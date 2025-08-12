import random

choices = ["rock", "paper", "scissors"]
user_score = comp_score = 0

while True:
    user = input("\nRock, paper, or scissors? ").lower()
    if user not in choices:
        print("Invalid choice.")
        continue
    comp = random.choice(choices)
    print(f"You: {user}  |  Computer: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    print(f"Score: You {user_score} - {comp_score} Computer")
    if input("Play again? (y/n): ").lower() != "y":
        break