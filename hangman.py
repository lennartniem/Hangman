import random
from art import art

def main():
    word = chooseword().lower()
    length = len(word)
    output = ["_"] * length
    guesses = []
    count_wrong = 0
    while count_wrong < 6 and "_" in output:
        progress(count_wrong, output, guesses)
        guess = input("Guess a letter or final word: ").lower()
        result = guessing(guess, word, guesses, output)
        if result == False:
            count_wrong += 1
    progress(count_wrong, output, guesses)
    if count_wrong == 6:
        print(f"You lose! The word was {word}")
    else:
        print(f"You win! The word was {word}")

def chooseword():
    with open("words.txt") as file:
        words = []
        for line in file:
            words.append(line.strip())
    return random.choice(words)

def guessing(guess, word, guesses, output):
    if not guess.isalpha():
        print("Letters only!")
        return None
    if len(guess) == 1:
        if guess in guesses:
            print("Already guessed!")
            return None
        guesses.append(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if guess == letter:
                    output[i] = letter
            return True
        else:
            print("Not in word")
            return False
    else:
        if guess == word:
           output[:] = list(word)
           return True
        else:
            print("Wrong word")
            return False

def progress(count_wrong, output, guesses):
    print(art[count_wrong])
    print(" ".join(output))
    print("Already guessed:", guesses)


if __name__ == "__main__":
    main()
