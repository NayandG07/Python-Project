import random

def number_guessing_game():
    print("Welcome to the Enhanced Number Guessing Game!")
    print("I will choose a number, and you have to guess it.\n")

    while True:
        # Select difficulty level
        print("Select Difficulty Level:")
        print("1. Easy (15 attempts)")
        print("2. Medium (10 attempts)")
        print("3. Hard (5 attempts)")
        try:
            difficulty = int(input("Enter your choice (1/2/3): "))
            if difficulty == 1:
                attempts = 15
            elif difficulty == 2:
                attempts = 10
            elif difficulty == 3:
                attempts = 5
            else:
                print("Invalid choice. Please select 1, 2, or 3.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3).\n")
            continue

        # Generate a random number
        number_to_guess = random.randint(1, 20)
        print("\nI have chosen a number between 1 and 20.")
        print(f"You have {attempts} attempts. Good luck!\n")

        # Initialize score
        score = 0
        hint_used = False

        # Start guessing
        while attempts > 0:
            try:
                guess = int(input(f"Attempts remaining ({attempts}): Enter your guess: "))

                if guess < 1 or guess > 20:
                    print("Please guess a number between 1 and 20.\n")
                    continue

                if guess < number_to_guess:
                    print("Too low! Try again.\n")
                elif guess > number_to_guess:
                    print("Too high! Try again.\n")
                else:
                    # Player guessed correctly
                    score = attempts * 10
                    print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
                    print(f"Your score: {score} points.\n")
                    break

                # Provide a hint after 3 failed attempts
                if not hint_used and attempts <= 12:
                    hint = "even" if number_to_guess % 2 == 0 else "odd"
                    print(f"Hint: The number is {hint}.\n")
                    hint_used = True

            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            # Decrease attempts
            attempts -= 1

        if attempts == 0:
            print(f"😢 Sorry, you're out of attempts. The number was {number_to_guess}.\n")

        # Replay option
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thank you for playing! Goodbye!")
            break

# Run the game
number_guessing_game()
