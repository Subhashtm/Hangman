import random

# List of words for the game
words = ['language', 'love', 'programmer', 'gamer', 'challenge', 'obstacles']

# Choose a random word
word = random.choice(words).lower()
guessed_letters = []
lives = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while lives > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"Sorry, '{guess}' is not in the word. Lives left: {lives}")

    # Show current progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(display_word))

    if '_' not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Game over! The word was:", word)
