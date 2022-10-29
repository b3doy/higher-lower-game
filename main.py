import art
from game_data import data
import random
from os import system

# Generate a random account from the game data.
def random_account():
    return random.choice(data)


# Format account data into printable format.
def format_data(question):
    name = question["name"]
    desc = question["description"]
    country = question["country"]
    return f"{name}, a  {desc}, from {country}"


# Check if user is correct.
def check_answer(guess, question_a_followers, question_b_followers):
    if question_a_followers > question_b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Ask user for a guess.
def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    question_a = random_account()
    question_b = random_account()

    # Make game repeatable.
    while game_should_continue:
        question_a = question_b
        question_b = random_account()

        while question_a == question_b:
            question_b = random_account()

        question_1 = "Compare A: " + format_data(question_a)
        question_2 = "Against B: " + format_data(question_b)
        print(question_1)
        print(art.vs)
        print(question_2)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        question_a_followers = question_a["follower_count"]
        question_b_followers = question_b["follower_count"]
        correct_answer = check_answer(guess, question_a_followers, question_b_followers)

        # Clear screen between rounds.
        system("clear")
        # Score Keeping.
        print(art.logo)
        if correct_answer:
            score += 1
            print(f"You're right! current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final Score: {score}")


game()
