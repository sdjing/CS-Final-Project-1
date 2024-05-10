from typing import List

def calculate_grades(scores: List[int]) -> List[str]:
    """Calculate grades based on the scores."""
    best = max(scores)
    grades = []
    for score in scores:
        if score >= best - 10:
            grades.append('A')
        elif score >= best - 20:
            grades.append('B')
        elif score >= best - 30:
            grades.append('C')
        elif score >= best - 40:
            grades.append('D')
        else:
            grades.append('F')
    return grades
