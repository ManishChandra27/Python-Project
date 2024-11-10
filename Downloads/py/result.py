
import tkinter as tk

def show_result(score, total_questions):
    result_window = tk.Toplevel()  
    result_window.title("Quiz Result")
    
    result_label = tk.Label(result_window, text=f"Your Score: {score} out of {total_questions}", font="Arial 20", fg="green")
    result_label.pack(pady=20)
    
    close_button = tk.Button(result_window, text="Close", command=result_window.destroy, font="Arial 15", bg="#6A994E", fg="white")
    close_button.pack(pady=10)
    
    result_window.mainloop()

