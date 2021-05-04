def input_grades():
    i = 1
    total_grade = 0
    done = False
    while not done:
        grade = float(input('Please enter a grade({}/10): \n'.format(i)))
        if grade < 0 or grade > 100:
            print("The grade is invalid!")
        else:
            total_grade += grade
            i += 1
            if i == 11:
                done = True
    average_grade = total_grade/10
    return average_grade
