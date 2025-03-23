data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Dwayne Johnson', 'follower_count': 200, 'description': 'Actor and Wrestler', 'country': 'United States'},
    {'name': 'Ariana Grande', 'follower_count': 198, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 195, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 193, 'description': 'Reality TV Star and Businesswoman', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 190, 'description': 'Reality TV Star and Businesswoman', 'country': 'United States'},
    {'name': 'Lionel Messi', 'follower_count': 188, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Beyoncé', 'follower_count': 170, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Neymar', 'follower_count': 167, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'National Geographic', 'follower_count': 150, 'description': 'Magazine', 'country': 'United States'},
    {'name': 'Justin Bieber', 'follower_count': 145, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Kendall Jenner', 'follower_count': 140, 'description': 'Model', 'country': 'United States'},
    {'name': 'Taylor Swift', 'follower_count': 135, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Virat Kohli', 'follower_count': 133, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Nicki Minaj', 'follower_count': 130, 'description': 'Musician', 'country': 'Trinidad and Tobago'},
    {'name': 'Jennifer Lopez', 'follower_count': 126, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Khloé Kardashian', 'follower_count': 123, 'description': 'Reality TV Star', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'follower_count': 120, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Shakira', 'follower_count': 118, 'description': 'Musician', 'country': 'Colombia'},
    {'name': 'Drake', 'follower_count': 116, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Billie Eilish', 'follower_count': 110, 'description': 'Musician', 'country': 'United States'}
]

import random

score = 0
user_guessed_correct = True

while user_guessed_correct:
    celebrity1 = random.choice(data)
    print(f"Compare A: {celebrity1['name']}, a {celebrity1['description']}, from {celebrity1['country']}.")


    celebrity2 = random.choice(data)
    print(f"Against B: {celebrity2['name']}, a {celebrity2['description']}, from {celebrity2['country']}.")

    guess = (input("Who has more followers? Type A or B.")).upper()

    if guess == "A" and celebrity1['follower_count'] > celebrity2['follower_count']:
        score += 1
        print(f"You are right. Current score: {score}")
    elif guess == "B" and celebrity2['follower_count'] > celebrity1['follower_count']:
        print(f"You are right. Current score: {score}")
        score += 1
    else:
        user_guessed_correct = False
        print(f"Sorry, thats wrong. Final score: {score}")


