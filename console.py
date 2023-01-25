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



def checkWord(usrInput):
    word = fake.word()
    wrong_letters = []
    correct_letters = []
    guesses = 10
    genWordLength = len(word)

    for gen_letter in word: # iterating through the generated word
        for user in usrInput: # iterating through the user input

            if guesses != 0:
                if gen_letter == user:
                    correct_letters.append(user)

                elif gen_letter not in user:
                    guesses =- 1
                    wrong_letters.append(user)

                
                
def main():
    while True:
        user_input = input("...\t")


if __name__ == "__main__":
    main()