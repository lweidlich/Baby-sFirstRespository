"""
    [x] generate a word
    [x] check letter count for word generated
    [x] get letter input from user
    [] check letter for if it is in the generated word
    [x] keep track of inncorrect letters
    [x] keep track of correct letters
    [x] keep track of guesses left
    [] track when word is fully guessed
"""
from faker import Faker 

fake = Faker() 


wrong_letters = []
correct_letters = []

word = fake.word()
genWordLength = len(word)

def checkWord(usrInput):

    guesses = 10
    for gen_letter in word: # iterating through the generated word
        for user in usrInput: # iterating through the user input

            if guesses != 0:
                if gen_letter == user:
                    correct_letters.append(user)

                elif gen_letter not in user:
                    guesses =- 1
                    wrong_letters.append(user)

                elif len(correct_letters) == genWordLength:
                    print(f"correct! the word is {word}")

            elif guesses == 0:
                print("you are out of guesses!")
                break

                
                
def main():
    while True:
        print(correct_letters)
        user_input = input("...\t")

        if user_input == word:
            print("you win!")

        else:
            checkWord(user_input)


if __name__ == "__main__":
    main()