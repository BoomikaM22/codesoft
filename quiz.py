import tkinter as tk

class QuizApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Quiz Game")
        self.score = 0
        self.question_index = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct_answer": "Paris",
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": "Mars",
            },
            {
                "question": "How many continents are there on Earth?",
                "options": ["5", "6", "7", "8"],
                "correct_answer": "7",
            },
        ]

        self.label = tk.Label(window, text="", font=("Arial", 12))
        self.label.pack(pady=20)

        self.radio_var = tk.IntVar()

        self.option_buttons = []
        for i in range(4):
            option = tk.Radiobutton(window, text="", variable=self.radio_var, value=i)
            option.pack()
            self.option_buttons.append(option)

        self.next_button = tk.Button(window, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.display_question()

    def next_question(self):
        user_answer_index = int(self.radio_var.get())
        if user_answer_index >= 0:
            user_answer = self.questions[self.question_index]["options"][user_answer_index]
            correct_answer = self.questions[self.question_index]["correct_answer"]

            if user_answer == correct_answer:
                self.score += 1

        self.question_index += 1

        if self.question_index < len(self.questions):
            self.display_question()
        else:
            self.display_score()

    def display_question(self):
        question_data = self.questions[self.question_index]
        self.label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=i)

    def display_score(self):
        self.label.config(text=f"Your Score: {self.score}/{len(self.questions)}")
        self.next_button.config(text="Play Again", command=self.reset_quiz)

    def reset_quiz(self):
        self.score = 0
        self.question_index = 0
        self.display_question()
        self.next_button.config(text="Next", command=self.next_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
