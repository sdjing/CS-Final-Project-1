from input_verification import get_valid_scores
from grading import calculate_grades

def main():
    try:
        num_students = int(input("Total number of students: "))
        scores = get_valid_scores(num_students)
        grades = calculate_grades(scores)
        for i, (score, grade) in enumerate(zip(scores, grades), 1):
            print(f"Student {i} score is {score} and grade is {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid number of students.")

if __name__ == "__main__":
    main()

