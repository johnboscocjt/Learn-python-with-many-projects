# python quiz game
questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest egg?: ",
    "What is the most abundant gas in the Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = (
    ("C", "D", "A", "A", "B")
)

# what user will type
guesses = [
    
]

score = 0

question_num = 0

for question in questions:
    print("__________________________")
    print(question)
    for option in options[question_num]: 
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
        
    question_num += 1
    
    
print("____________________________")
print("           RESULT           ")
print("____________________________")

# iterate all the answers and the guesses
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()



score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
