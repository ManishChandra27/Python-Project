import tkinter as tk
from PIL import Image, ImageTk
from questions import get_random_question, reset_questions
from result import show_result

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("720x500")


        self.bg_image = Image.open("background.jpg")  
        self.bg_image = self.bg_image.resize((720, 500), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        
        
        self.score = 0
        self.total_questions = 0  

        self.create_intro_screen()

    def create_intro_screen(self):
        self.welcome_label = tk.Label(self.master, text="Welcome to the Quiz Game!", font="sans-serif 24 bold", bg="#fff8dc", fg="black")
        self.welcome_label.pack(pady=100)

        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz, font="Arial 20 bold", bg="#ccff00", fg="black")
        self.start_button.pack(pady=20)

    def start_quiz(self):
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        self.reset_quiz()

        self.create_quiz_ui()

        self.next_question()

    def create_quiz_ui(self):
        self.question_label = tk.Label(self.master, text="", font="Arial 18 bold", bg="#fff8dc", fg="black")
        self.question_label.pack(pady=100)

        self.answer_entry = tk.Entry(self.master, font="Arial 16 bold", bg="#fff8dc", fg="#a28200")
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font="Arial 15 bold", bg="#90EE90", fg="black")
        self.submit_button.pack(pady=45)

        self.feedback_label = tk.Label(self.master, text="", font="Arial 14", bg="#fff8dc", fg="yellow")
        self.feedback_label.pack(pady=5)

    def reset_quiz(self):
        reset_questions()  
        self.score = 0
        self.total_questions = 0  

    def next_question(self):
        question_data = get_random_question()  
        if question_data:
            question, self.answer = question_data
            self.total_questions += 1  
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END) 
        else:
          
            show_result(self.score, self.total_questions) 
            self.master.quit()  

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == self.answer.lower():
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect! Correct answer: {self.answer}", fg="red")
        
        
        self.master.after(500, self.next_question)  

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
