''' Align Online
    CS5001
    Sample code for Module 11: Dictionaries and Sets 
    
    Three examples for creating the same do_re_mi dictionaries in PythonDo-Re-Mi example of using Dictionaries in Python
'''

empty_dictionary = {}

# Example uses the {} to delimit a list of key:value pairs
do_re_mi_1 = {"do": "doe, a deer, a female deer",
              "re": "a drop of golden sun",
              "mi": "a name I call myself",
              "fa": "a long, long way to run"
              }


# Example uses the dict() function with a list of named parameters
do_re_mi_2 = dict(do="doe, a deer, a female deer", re="a drop of golden sun",
                  mi="a name I call myself", fa="a long, long way to run")

# Example uses the dict() with a list of 2-value lists as the parameter
do_re_mi_3 = dict([["do", "doe, a deer, a female deer"],
                   ["re", "a drop of golden sun"],
                   ["mi", "a name I call myself"],
                   ["fa", "a long, long way to run"]])
