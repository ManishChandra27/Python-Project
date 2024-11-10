import random
questions = [
    ("What is the capital of France?", "paris"),
    ("What is 2 + 2?", "4"),
    ("What is the capital of Japan?", "tokyo"),
    ("What is the largest planet in our solar system?", "jupiter"),
    ("Who wrote 'Romeo and Juliet'?", "william shakespeare"),
    ("What is the capital of France?", "paris"),
    ("What is 2 + 2?", "4"),
    ("What is the capital of Japan?", "tokyo"),
    ("What is the capital of Japan?", "tokyo"),
    ("What is the largest planet in our solar system?", "jupiter"),
    ("Who wrote 'Romeo and Juliet'?", "william shakespeare"),
    ("What is the chemical symbol for water?", "h2o"),
    ("Who painted the Mona Lisa?", "leonardo da vinci"),
    ("What is the square root of 64?", "8"),
    ("What is the hardest natural substance on Earth?", "diamond"),
    ("Who is known as the father of computers?", "charles babbage"),
    ("What is the largest ocean on Earth?", "pacific"),
    ("Which country is known as the Land of the Rising Sun?", "japan"),
    ("In what year did the Titanic sink?", "1912"),
    ("Who discovered electricity?", "benjamin franklin"),
    ("What is the largest desert in the world?", "sahara"),
    ("What is the speed of light in a vacuum?", "299792458 m/s"),
    ("Who was the first president of the United States?", "george washington"),
    ("What is the longest river in the world?", "nile"),
    ("What is the capital of France?", "paris"),
    ("How many continents are there?", "7"),
    ("What is the smallest country in the world?", "vatican city"),
    ("What is the main ingredient in guacamole?", "avocado"),
    ("Who invented the telephone?", "alexander graham bell"),
    ("What is the currency of the United Kingdom?", "pound"),
    ("Who was the first man to walk on the moon?", "neil armstrong"),
    ("What is the largest land animal?", "african elephant"),
    ("Which element has the chemical symbol 'O'?", "oxygen"),
    ("Who is the author of 'Harry Potter'?", "j.k. rowling"),
    ("What is the capital of Canada?", "ottawa"),
     ("How many states are in the United States?", "50"),
     ("Who was the first woman to fly solo across the Atlantic?", "amelia earhart"),
     ("What is the tallest mountain in the world?", "mount everest"),
     ("What is the main gas in Earth's atmosphere?", "nitrogen"),
     ("What is the longest river in the United States?", "missouri"),
]


unanswered_questions = questions[:]

def get_random_question():
    if unanswered_questions:
        question_data = random.choice(unanswered_questions)
        unanswered_questions.remove(question_data) 
        return question_data
    else:
        return None

def reset_questions():
    global unanswered_questions
    unanswered_questions = questions[:]  
    random.shuffle(unanswered_questions)  
