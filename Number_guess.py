import random
# Generate a random number between 1 and 100
secret_numbers = random.randint(1,100)

print("Welcome to the Number guessing game ")

print("I have chosen number between 1 to 100 . Can you guess it ? ")

attempts = 0
while  True:
    # Get the user's guess
    guess = input("Enter your guess (or 'quit' to exit): ")
    if guess.lower() == 'quit':
        print(f'you gave up ! The secret number was {secret_numbers}')
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    attempts += 1
    # Check if the guess is correct
    if guess == secret_numbers:
        print(f"Congratulation! you gussed the number {secret_numbers} in {attempts } attempts")
        break
    elif guess < secret_numbers:
        print(f"Too low! Try again. The secret number was {secret_numbers}")
    else:
        print(f"Too high! Try again. The secret number was {secret_numbers}")
# The game continues until the user guesses the correct number or types 'quit' to exit.
      




