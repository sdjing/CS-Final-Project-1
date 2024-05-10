import tkinter as tk
from tkinter import messagebox
from input_verification import get_valid_scores
from grading import calculate_grades
#Gui app
class StudentGraderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grader")

        self.num_students_label = tk.Label(root, text="Total number of students:")
        self.num_students_label.pack()

        self.num_students_entry = tk.Entry(root)
        self.num_students_entry.pack()

        self.score_entries = []

        self.submit_students_button = tk.Button(root, text="Submit Students", command=self.create_score_entries)
        self.submit_students_button.pack()

        self.calculate_button = tk.Button(root, text="Calculate Grades", command=self.calculate_grades)
        self.calculate_button.pack()

        self.results_text = tk.Text(root, height=10, width=50)
        self.results_text.pack()

    def create_score_entries(self):
        num_students = int(self.num_students_entry.get())
        for i in range(num_students):
            label = tk.Label(self.root, text=f"Enter score for student {i+1}:")
            label.pack()
            entry = tk.Entry(self.root)
            entry.pack()
            self.score_entries.append(entry)
        self.submit_students_button.config(state="disabled")

    def get_scores_from_entries(self):
        scores = []
        for entry in self.score_entries:
            try:
                score = int(entry.get())
                if 0 <= score <= 100:
                    scores.append(score)
                else:
                    messagebox.showerror("Error", "Invalid score! Score must be between 0 and 100.")
                    return None
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Please enter valid integer scores.")
                return None
        return scores

    def calculate_grades(self):
        scores = self.get_scores_from_entries()
        if scores:
            grades = calculate_grades(scores)
            result = "\n".join([f"Student {i+1} score is {score} and grade is {grade}" for i, (score, grade) in enumerate(zip(scores, grades))])
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, result)

def main():
    root = tk.Tk()
    app = StudentGraderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
