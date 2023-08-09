def to_play():
    print("Welcome to the hangman game!")

    secret_word = "neuro transmitter".upper()
    exact_lettes = ["_" if letter != " " else " " for letter in secret_word]

    hanged = False
    hit: bool = False
    error = 0

    print(exact_lettes)

    while not hanged and not hit:

        guess: str = input("Choose a letter?")
        guess = guess.strip().upper()

        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if guess == letter:
                    exact_lettes[index] = letter
                index += 1
        else:
            error += 1
            print(f'Oops, you got it wrong! Attempts {5 - error} are missing.')

        hanged = error == 5
        hit = "_" not in exact_lettes
        print(exact_lettes)

    if hanged:
        print("The game is over, you lost!")

    if hit:
        print("You won the Game!")
        print("End of the game!")


if __name__ == "__main__":
    to_play()
