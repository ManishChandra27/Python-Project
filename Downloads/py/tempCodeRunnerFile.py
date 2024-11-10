import tkinter as tk
from PIL import Image, ImageTk
from questions import get_random_question, reset_questions
from result import show_result

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("720x500")

        # Load background image
        self.bg_image = Image.open("background.jpg")  # Ensure you have a valid image path
        self.bg_image = self.bg_image.resize((720, 500), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        # Background label
        self.bg_label = tk.Label(master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        
        # Score
        self.score = 0
        self.total_questions = 0  # To keep track of the total number of questions

        # Create the intro screen
        self.create_intro_screen()

    def create_intro_screen(self):
        # Welcome message
        self.welcome_label = tk.Label(self.master, text="Welcome to the Quiz Game!", font="sans-serif 24 bold", bg="#fff8dc", fg="black")
        self.welcome_label.pack(pady=100)

        # Start button
        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz, font="Arial 20 bold", bg="#ccff00", fg="black")
        self.start_button.pack(pady=20)

    def start_quiz(self):
        # Remove the intro screen widgets
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        # Reset quiz state
        self.reset_quiz()

        # Create quiz UI
        self.create_quiz_ui()

        # Load the first question
        self.next_question()

    def create_quiz_ui(self):
        # Question label
        self.question_label = tk.Label(self.master, text="", font="Arial 18 bold", bg="#fff8dc", fg="black")
        self.question_label.pack(pady=100)

        # Answer entry
        self.answer_entry = tk.Entry(self.master, font="Arial 16 bold", bg="#fff8dc", fg="#a28200")
        self.answer_entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font="Arial 15 bold", bg="#90EE90", fg="black")
        self.submit_button.pack(pady=45)

        # Feedback label
        self.feedback_label = tk.Label(self.master, text="", font="Arial 14", bg="#1B3A4B", fg="yellow")
        self.feedback_label.pack(pady=5)

    def reset_quiz(self):
        reset_questions()  # Reset questions if needed
        self.score = 0
        self.total_questions = 0  # Reset the total questions count

    def next_question(self):
        question_data = get_random_question()  # Get a random question
        if question_data:
            question, self.answer = question_data
            self.total_questions += 1  # Increment the total question count
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)  # Clear the previous answer
        else:
            # All questions answered, show the result
            show_result(self.score, self.total_questions)  # Pass score and total questions to show_result
            self.master.quit()  # Quit the game window

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == self.answer.lower():
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect! Correct answer: {self.answer}", fg="red")
        
        # Wait for feedback and then load the next question
        self.master.after(500, self.next_question)  # Delay next question for 500ms

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
