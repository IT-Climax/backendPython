import random


def guess_the_word():
    # List of possible words
    words = ["play", "on top", "understanding", "ruby", "swift", "turn", "Alic", "wonderful", "complain", "misunderstand",  "no", "pet", "pseudoscientific", "Disentanglement",]
    print(words)
    chosen_word = random.choice(words)
    word_length = len(chosen_word)

    # Create a list of underscores to represent the word
    display_word = ["_"] * word_length

    # Set the number of allowed guesses
    max_guesses = 4
    guessed_letters = set()

    print("Welcome to Guess the Word!")
    print(f"The word has {word_length} letters.")

    while max_guesses > 0 and "_" in display_word:
        # Display the current state of the word
        print(" ".join(display_word))

        # Prompt the player to guess a letter
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the word
        if guess in chosen_word:
            print(f"Good guess! {guess} is in the word.")
            # Update the display_word with the correct letter
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display_word[i] = guess
        else:
            max_guesses -= 1
            print(f"Oops! {guess} is not in the word. You have {max_guesses} guesses left.")

        print()

    # Game result
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f"Sorry, you're out of guesses. The word was: {chosen_word}")



guess_the_word()


