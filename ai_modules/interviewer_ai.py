import random

QUESTIONS = [
    "Introduce yourself briefly",
    "Explain polymorphism",
    "Describe a team project you handled",
    "What is your career goal?"
]

def next_question():
    return random.choice(QUESTIONS)