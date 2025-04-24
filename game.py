import random
 
def guess_the_number():
    """A simple number guessing game."""
 
    secret_number = random.randint(1, 20)
    guesses_left = 3
 
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20.")
 
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
 
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {3 - guesses_left +1} tries. The number was {secret_number}.")
            return  # End the game if the guess is correct
 
        guesses_left -= 1
 
    print(f"\nYou ran out of guesses. The number was {secret_number}.")
 
 
if __name__ == "__main__":
    guess_the_number()