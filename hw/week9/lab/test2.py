def flesch_grade(index):
    '''
    Function: flesch_grade
       Caclulates the Flesch grade (educational level)
    Parameters:
       index (float) -- Flesch readability index
    Returns the educational level
    '''
    # TODO: Implement me!!
    if isinstance(index,float):
        index = float(index)
    else:
        raise TypeError('Index should be a float')

flesch_grade('sss')