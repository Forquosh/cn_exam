import json
import random
import time

# Colors
class colors:
    CORRECT = '\033[92m'
    INCORRECT = FAILED = '\033[91m'
    NORMAL = '\033[0m'
    PASSED = '\033[94m'

print("\nWelcome to the Computer Networks quiz!")
print("You will be asked a series of multiple choice questions, and you must answer them correctly.")
print("Write (in lowercase) all the corresponding letter/s of the answer/s you think is/are correct.")

# Store the questions in an array
questions = []
with open('questions.json', 'r', encoding='utf-8-sig') as f:
    for q in json.load(f):
        questions.append(q)

print("\nTotal nr. of questions: " + str(len(questions)))

while True:
    # Ask user how many questions they want to answer
    user_input = input("How many questions do you want to answer?\n-> ")
    nr_questions = len(questions)
    try:
        user_input = int(user_input)
        if user_input <= nr_questions:
            nr_questions = user_input
    except ValueError:
        print("Incorrect input, please try again...\n")
        continue

    score = 0
    mistakes = []
    for i in range(nr_questions):
        print(colors.NORMAL + "\n-- Question " + str(i + 1) + "/" + str(nr_questions) + " --")

        # Select a random question
        q = random.choice(questions)

        # Removes the selected question from the set of questions
        # If user chooses to play again, the already answered questions won't get chosen again
        questions.remove(q)

        # Display the question
        print(colors.NORMAL + q['question'])
        
        # Display the answer
        if q['answers'] != []:
            # For each question display the answers, and in front of each one, display the corresponding character
            # first answer will correspond to 'a', the second to 'b' etc.
            for i in range(len(q['answers'])):
                print(chr(ord('a') + i) + ") " + q['answers'][i])
        
        # Get user input
        answer = input("Your answer: ")
        # Check user input
        if answer == q['correct']:
            print(colors.CORRECT + "Correct!")
            score += 1
        else:
            print(colors.INCORRECT + "Incorrect!")
            print("The correct answer was: " + q['correct'])
            mistakes.append((q, answer))

    # Convert user score to percentage
    score = score / nr_questions * 100
    if(score >= 50):
        print(colors.PASSED + "\nYou got " + str(score) + "%" + " of questions right!\n You passed! :D\n")
    else:
        print(colors.FAILED + "\nYou only got " + str(score) + "%" + " of questions right.\n You failed. :/\n")


    # Ask user to review mistakes
    user_input = input(colors.NORMAL + "Do you want to review your mistakes?(y/n): ")
    if user_input == "y":
        for (q, answer) in mistakes:
            print(colors.NORMAL + q['question'])
            for i in range(len(q['answers'])):
                print(chr(ord('a') + i) + ") " + q['answers'][i])
            print("Your answer was: " + colors.INCORRECT + answer)
            print(colors.NORMAL + "The correct answer was: " + colors.CORRECT + q['correct'] + '\n')

    # Ask user if they want to play again
    user_input = input(colors.NORMAL + "Do you want to play again?(y/n): ")
    if user_input == "n":
        print("You shall (definitely) pass!")
        time.sleep(0.75)
        break
    else:
        print("Here we go again...")
        time.sleep(1.25)