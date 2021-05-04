''' Align Online
    CS5001
    Sample code for Module 11: Dictionaries and Sets 
    Implementation of a grade book of sorts using parallel lists.
    In this example, there is an error in the delete_student function
'''

# Storing students and grades in parallel lists where the position of
# the student in the names list is the same as the position of the grade
# of that student in the grades list
names = ["Grace Hopper", "Ada Lovelace", "Alan Turing"]
grades = ["A", "A-", "C"]


def get_grade(req_name):
    ''' Function get_grade
        Parameters:  req_name, the name of the student's whose grade you want
        Returns:  nothing
    '''
    for i in range(len(names)):
        if names[i] == req_name:
            print("student", names[i], "earned", grades[i])
            return
    print("Did not find record for", req_name)


def delete_student(req_name):
    ''' Function delete_student
        Parameters:  req_name, the name of the student to delete
        Returns:  nothing
    '''
    for i in range(len(names)):
        if names[i] == req_name:
            del names[i]
            return
    print("Did not find record for", req_name)

