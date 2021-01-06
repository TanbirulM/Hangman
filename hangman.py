import random
import string
from words import word_list


def get_word():
    # randomly chooses a word from the list
    word = random.choice(word_list)  
    return word.upper()


def play_game():
    word = get_word()
    alphabet = set(string.ascii_uppercase)
    chosen_letters = set(word)  # letters in the word
    guessed_letters = set()

    lives = 6

    while len(chosen_letters) > 0 and lives > 0:
        print('You have used', (6 - lives), 'out of 6 lives.')
        print('You have used these letters: ', ' '.join(guessed_letters))

        # ie (W R - N G)
        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in chosen_letters:
                chosen_letters.remove(user_letter)
                print('')

            else:
                lives -= 1  
                print('Your letter,', user_letter, 'is not in the word.')

        elif user_letter in guessed_letters:
            print('You have already used that letter. Guess again.')

        else:
            print('That is not a valid input.')

    if lives == 0:
        print('\nYou ran out of lives and died! \nThe word was', word)
    else:
        print('\nCongratulations! You guessed the word', word, 'and lived!')


def main():
    play_game()

# Standard call for main() function
if __name__ == '__main__':
    main()
