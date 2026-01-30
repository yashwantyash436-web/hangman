import random

# Step 1: Word list
word_list = ["camel", "yashwanth", "pencil", "python", "hangman"]

# Step 2: Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Step 3: Create blanks
display = []
for _ in range(word_length):
    display.append("_")

# Step 4: Game variables
lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print(display)

# Step 5: While loop for game continuation
while lives > 0 and "_" in display:
    guess = input("\nGuess a letter: ").lower()

    # If letter already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue
    else:
        guessed_letters.append(guess)

    # Step 6: Check guessed letter
    found = False
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
            found = True

    if not found:
        lives -= 1
        print(f"❌ Wrong guess. Lives left: {lives}")

    print(display)

# Step 7: Game result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
