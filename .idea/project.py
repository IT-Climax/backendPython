import random

def rand_guess():
    # list of words that are to display
    words = ["play", "wonderful", "advantage", "thanks", "bully", "light", "laugh"]
    print(f"{words}")
    # it is expected to print the list of words
    selected=random.choice(words)
    word_length= len(selected)
    chosen_word= ['-'] * word_length


rand_guess()



