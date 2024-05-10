from typing import List

def get_valid_scores(num_students: int) -> List[int]:
    """Prompt the user to enter scores for each student."""
    scores = []
    while len(scores) < num_students:
        score_input = input(f'Enter score for student {len(scores) + 1}: ').strip()
        try:
            score = int(score_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Invalid score Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer score.")
    return scores
