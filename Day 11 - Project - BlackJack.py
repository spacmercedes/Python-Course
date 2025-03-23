import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, oponent has black jack"
    elif u_score == 0:
        return "Win with black jack"
    elif u_score > 21:
        return "ypou went over u lose"
    elif c_score > 21:
        return "Oponent went over, you win"
    elif u_score > c_score:
        return "Ypu win"
    else:
        return "You lose"


user_cards = []
computer_cards = []
is_game_over = False
computer_score = -1
user_score = -1

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type y to get other card, n to pass")
        if user_should_deal == "y":
            user_cards.append(deal_cards())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append((deal_cards()))
    computer_score = calculate_score(computer_cards)

print(compare(user_score,computer_score))