# Hangman Game
#### Video Demo:  https://www.youtube.com/watch?v=f7jVf10nqyc
#### Description:
This project is a simple one player Hangman game where a word is randomly chosen from a file of words each over five letters long. The aim of the game is to guess the word letter by letter before making six incorrect guesses. It displays the word in a series of underscores, which get replaced one by one if a letter is guessed correctly.

When a correct letter is guessed, the program reveals the letter's position or positions in the word, but if the guessed letter is wrong, the player loses one of their remaining guesses and ascii art of a hangman is displayed. Whether the guessed letter was right or wrong, it gets added to a list of guessed letters, and if that same letter is guessed again, the player gets told they have already guessed this.

If the player guesses more than one character, this is treated as a guess for the final word, and if it is right, the program ends and outputs a win message. If not, the player loses another of their remaining guesses.

The words.txt file contains all the possible word choices for the game, and the art.py file contains the different stages of the ascii art for the hangman, depending on how many incorrect guesses have been made.

The main() function controls the whole game and prints the final win or lose messages. The chooseword() function opens the words.txt text file and reads each line and then randomly chooses one word to be the secret word for that game. The guessing() function takes the player's input and checks if it is a character or word, then checks if that character is correct or not. It then updates the guessed letters list and prints feedback on the player's guess. The progress() function outputs the current state of the game, including the ascii art, what letters have been guessed so far and the letters already revealed.

I debated whether to allow the player to guess a whole word if they want to, or only one letter at a time. I chose to allow them to, as it gives the player more freedom and a bit of a riskier choice if they believe to have the whole word. So if a player is confident, they can choose to guess the whole word to save time, at the risk of losing a remaining guess and gaining no information. I also chose to keep the words and ascii art in separate files to make my main code look cleaner and lets me change them without having to go through the whole code.

The program also checks whether the player's input is only letters, and rejects if it isn't, without a penalty to the player. I included this to prevent invalid input from affecting the game and to make the game more clear for the user.
