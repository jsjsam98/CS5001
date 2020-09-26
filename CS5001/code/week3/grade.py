def grade(score):
    if score >= 93:
        return 'A'
    elif score >= 90 and score <= 92.99:
        return 'A-'
    elif score >= 86 and score <= 89.99:
        return 'B+'
    elif score >= 82 and score <= 85.99:
        return 'B'
    elif score >= 77 and score <= 81.99:
        return 'B-'
    elif score >= 73 and score <= 76.99:
        return 'C+'
    elif score >= 69 and score <= 72.99:
        return 'C'
    elif score >= 65 and score <= 68.99:
        return 'C-'
    elif score >= 0 and score <= 64.99:
        return 'F'
