import random

def guess_game():
  secret_number = random.randint (1, 10)

  guess_times = 0

  while True:
    guess_times += 1
    guess = int(input("Enter the guess: "))

    if guess < secret_number:
      print("The guess is too low!")

    elif guess > secret_number:
      print("The guess is too high!")

    else:
      print(f"Congratulations. You have entered the correct number: {guess}")

guess_game()
      



    




