
import random

def hangman():
    words = ['apple', 'banana', 'orange', 'mango', 'strawberry', 'kiwi']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    while tries > 0:
        # Display the current progress of the word
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord:", display_word)

        if display_word == word:
            print("Congratulations! You guessed the word correctly.")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)

            if guess in word:
                print("Correct guess!")
            else:
                tries -= 1
                print("Incorrect guess. You have", tries, "tries remaining.")

        else:
            print("Invalid input. Please enter a single letter.")

    else:
        print("Game over! You ran out of tries. The word was:", word)

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def main():
    print("Welcome to Hangman!")

    while True:
        hangman()
        if not play_again():
            break

    print("Thank you for playing Hangman!")

if __name__ == '__main__':
    main()

