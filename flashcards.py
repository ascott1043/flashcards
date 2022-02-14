import random
from time import sleep

with open("flashcards.txt") as file:
    acronyms = []
    for line in file:
        line = line.replace("\n", "")
        acronyms.append(line.split("\t"))


def flash_card_app():
    print("\nWelcome to flash card app!\nType 'hint' for a hint, 'quit' to quit\n")
    sleep(1)
    while True:
        card = random.randint(1, 399)
        question = acronyms[card]
        answer = input(question[0] + "\t")

        if answer.lower() == "quit":
            break

        if answer.lower() == "hint":
            print(question[2])
            answer = input("\t")

        if answer.lower() == question[1].lower():
            print("\nCorrect!")

        else:
            print("\nWrong! Correct answer: " + question[1])
        print("\n")
        sleep(1)


if __name__ == "__main__":
    flash_card_app()
