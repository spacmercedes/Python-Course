import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type easy or hard.")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 10")
    answer = random.randint(1,100)
    print(answer)

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guesss the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have no guesses")
            return

game()












# print("Welcome to the Number Guessing Game")
# print("I am thinking of a number between 1 and 10")
# number_to_guess = random.randint(1,100)
# print(number_to_guess)
#
# difficulty = (input("Choose difficulty:  hard or easy")).lower()
#
# attempts = 0
# if difficulty == "easy":
#     attempts += 10
# elif difficulty == "hard":
#     attempts += 5
#
#
# user_not_guessed = True
# print(difficulty)
# print(attempts)
#
# if attempts == 0:
#     print("You lost")
# else:
#     for attempt in range(attempts):
#         while user_not_guessed:
#             guess = int(input("Make a guess: "))
#             if guess > number_to_guess:
#                 print("Too high")
#                 attempts -= 1
#                 print(f"You have {attempts} left")
#             elif guess < number_to_guess:
#                 print("Too low")
#                 attempts -= 1
#                 print(f"You have {attempts} left")
#             elif guess == number_to_guess:
#                 print("You won")
#                 user_not_guessed = False
#
#
