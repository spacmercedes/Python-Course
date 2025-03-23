import random
word_list = ["aardsds","baboon","camel"]
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)



game_over = False
correct_letters =[]

while not game_over:
    guess = (input("Guess a letter: ")).lower()
    display = ''
    for letter in chosen_word:
        if(guess == letter):
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display +="_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])