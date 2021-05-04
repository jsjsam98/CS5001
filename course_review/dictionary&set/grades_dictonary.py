''' Align Online
    CS5001
    Sample code for Module 11: Dictionaries and Sets 
    Implementation of a grade book of sorts using dictionary
    The functions are not quite equivalent to the parallel list
    implementation since they do not print out when a record
    is not found.
'''

# Storing students and grades in a dictionary
grades = {"Grace Hopper": "A", "Ada Lovelace": "A-", "Alan Turing": "C"}


def get_grade(req_name):
    ''' Function get_grade
        Parameters:  req_name, the name of the student's whose grade you want
        Returns:  nothing
    '''
    print("student", req_name, "earned", grades[req_name])


def delete_student(req_name):
    ''' Function delete_student
        Parameters:  req_name, the name of the student to delete
        Returns:  nothing
    '''
    del grades[req_name]

