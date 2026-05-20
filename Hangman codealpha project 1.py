
import random

# Step 1: Predefined word list
words = ["python", "internship", "hangman", "developer", "program"]

# Step 2: Randomly choose a word
chosen_word = random.choice(words)

# Step 3: Game variables
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect attempts. Let's start!\n")

while attempts > 0:
    display_word = ""

    # Step 4: Display guessed letters
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Step 5: Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Step 6: Check correct or incorrect
    if guess not in chosen_word:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}\n")
    else:
        print("✅ Correct guess!\n")

# Step 7: If user loses
if attempts == 0:
    print(f"💀 Game Over! The word was: {chosen_word}")