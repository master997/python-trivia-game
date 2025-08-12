#list of questions
#store answers
#randomly pick questions
#ask the questions
# see if they corrrect
# keep track of score
# tell user their score


import random
questions = {
    "What is the capital of France?": "paris",  
    "What is the capital of Germany?": "berlin",
    "What is the capital of Italy?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the capital of Portugal?": "lisbon",
    "What is the capital of Greece?": "athens",
    "What is the capital of Turkey?": "ankara",
    "What is the capital of Egypt?": "cairo",
    "What is the capital of Saudi Arabia?": "riyadh",
    "What is the capital of Qatar?": "doha",
    "What is the capital of United Arab Emirates?": "abu dhabi",
    "What is the capital of Oman?": "muscat",
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list,total_questions)

    for idx, question in enumerate(selected_questions):
        print(f'{idx+1}. {question}')
        user_answer = input('Your answer: ').lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")
    
    print(f'game over! Your score is {score} out of {total_questions}.')



python_trivia_game()