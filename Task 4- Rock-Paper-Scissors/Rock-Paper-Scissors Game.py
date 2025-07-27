import random

# Available choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0
round_num = 1

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")

# Main game loop
while True:
    print(f"\n🔁 Round {round_num}")
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"🧍 You chose: {user_choice}")
    print(f"🤖 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "✅ You win!"
        user_score += 1
    else:
        result = "❌ You lose!"
        computer_score += 1

    # Display result
    print("📢 Result:", result)
    print(f"🏆 Score - You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n🎉 Final Score:")
        print(f"🧍 You: {user_score} | 🤖 Computer: {computer_score}")
        print("👋 Thanks for playing!")
        break

    round_num += 1