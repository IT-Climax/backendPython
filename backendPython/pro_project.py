import random

def Guess_game():
    print("welcome to the Guess game")
    print("Do you wish to continue ?")
    command=input("> ")
    if command.lower() == "no":
        print("thank you")
    else:
        print(f"choose from the list below")
        numbers = ["thousand", "hundred", "million", "tens", "hundreds", "unit"]
        chose_words=random.choice(numbers)
        print(f"{numbers}")
        word_length= len(chose_words)
        word = ["_"] * word_length
        max_guesses = 4
        guessed_letters = set()

        while max_guesses > 0 and "_" in word:
            # Display the current state of the word
            print(" ".join(word))

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
            if guess in chose_word:
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


Guess_game()