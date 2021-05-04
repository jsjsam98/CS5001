'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 12 -- Book

This program defines a Book Class
'''
from readability import *
import os


class Book:
    ''' Class Book represents a book published by Random House Books.
        Attributes: isbn, title, author, year, format, filename
        Methods: get_title, get_author, get_year, get_format, get_filename,
                get_readability_grade, get_index
    '''

    def __init__(self, isbn, title, author, year, format, filename):
        '''
        Constructor -- creates new instances of book
        Parameters:
           self -- the current object
           isbn -- a 13-digit number
           title -- title of the book
           author -- author of the book
           year -- the year when it published
           format -- format of the book
           filename -- the name of the file
        '''
        format_list = {"Hardcover", "Softcover", "Kindle", "PDF"}
        if type(isbn) is not str or isbn == "" or isbn[0:3] != "978"\
           and isbn[0:3] != "979" or len(isbn) != 13:
            raise ValueError("Invalid ISBN provided to this Book")
        if type(title) is not str or title == "":
            raise ValueError("Invalid title provided to this Book")
        if type(author) is not str or author == "":
            raise ValueError("Invalid author provided to this Book")
        if type(year) is not int:
            raise ValueError("Invalid year provided to this Book")
        if type(format) is not str or format not in format_list:
            raise ValueError("Invalid format provided to this Book")
        if type(filename) is not str or filename == "":
            raise ValueError("Invalid filename provided to this Book")
        if not os.path.exists(filename):
            raise ValueError("Invalid filename provided to this Book")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.format = format
        self.filename = filename

    def get_title(self):
        '''
        Method -- get title of the book
        Parameters:
           self -- the current object
        '''
        return self.title

    def get_author(self):
        '''
        Method -- get author of the book
        Parameters:
           self -- the current object
        '''
        return self.author

    def get_year(self):
        '''
        Method -- get year of the book
        Parameters:
           self -- the current object
        '''
        return self.year

    def get_format(self):
        '''
        Method -- get format of the book
        Parameters:
           self -- the current object
        '''
        return self.format

    def get_filename(self):
        '''
        Method -- get filename of the book
        Parameters:
           self -- the current object
        '''
        return self.filename

    def get_readability_grade(self):
        '''
        Method -- get flesh_grade of the book
        Parameters:
           self -- the current object
        '''
        try:
            # calculate the flesh_grade
            filename = self.filename
            input_file = open(filename, 'r')
            filedata = input_file.readlines()
            sentences, words, syllables = analyze_file_data(filedata)
            index = flesch_index(sentences, words, syllables)
            grade = flesch_grade(index)
            input_file.close()
            return grade
        # to pass CodePost I cannot use a bare except
        except ValueError:
            raise ValueError(
                'Error occurred while calculating the Flesch grade for {}'
                .format(title))

    def get_index(self):
        '''
        Method -- get index of the book
        Parameters:
           self -- the current object
        '''
        try:
            filename = self.filename
            input_file = open(filename, 'r')
            filedata = input_file.readlines()
            content = ''
            for i in filedata:
                i = i.strip().lower()
                content += i + '\n'
            content_list = content.split()

            # add a comma in the mark list
            mark = [':', ';', '.', '?', '!', ',']
            index = {}
            count = 0
            for i in content_list:
                if i[-1] in mark:
                    i = i[0:-1]
                if i[-1] == '-':
                    i = content_list[count][0:-1] + content_list[count + 1]
                    del content_list[count + 1]
                if i in index:
                    index[i] += 1
                else:
                    index[i] = 1
                count += 1
            return index
        # to pass CodePost I cannot use a bare except
        except ValueError:
            raise ValueError(
                'Error occurred while generating the index for {}'
                .format(title))

    def __str__(self):
        '''
        Method -- returns a string that represents this book
        Parameters:
           self -- the current object
        '''
        output = self.title + " by " + self.author + ", " + str(self.year) +\
            "\n" + "ISBN: " + self.isbn + ", " + self.format +\
            ", " + self.get_readability_grade() + ", " + self.filename

        return output
