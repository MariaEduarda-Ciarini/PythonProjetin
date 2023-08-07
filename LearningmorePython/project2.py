import random

secret_number =  random.randrange(1, 151)
total_attempts = 0
points = 1000

print("What difficulty level do you choose to play?")
print("(1) Easy (2) Medium (3) Hard")

level = int(input("Choose the level: ", ))

if (level == 1):
    total_attempts = 20
elif(level == 2):
    total_attempts = 10
else:
    total_attempts = 3


for game_round in range(1, total_attempts + 1):
    print("Attempt {} of {}".format(game_round, total_attempts))
    guess_str = input("Enter a number between 1 to 150: ")
    print("You typed", guess_str)
    guess = int(guess_str)

    if (guess < 1 or guess > 151):
        print("You must enter a number between 1 to 150!")
        continue

    hit = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

    if hit:
        print("You're right and made {} points!".format(points))
        break
    else:
        if bigger:
            print("You missed! The kick was bigger than the secret number.")
        elif smaller:
            print("You missed! The kick was lower than the secret_number.")
            points_lost = abs(secret_number -  guess)
            points = points - points_lost

print("Finish game!")
