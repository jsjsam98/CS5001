"""
This file defines a class called Book
Author: Tianyu Tan
Course: CS5001-SP20
Lab12
"""
from readability import *


class Book:
    """
    Class Book
    Attributes: isbn, title, author, year, format, filename,
                flesch_grade
    Methods: get_title, get_author, get_year, get_format,
            get_readability_grade, get_index
    """
    def __init__(self, isbn, title, author, year, format, filename):
        """
        Constructor: take parameters as attributes and work out file_data
                     and flesch_grade as attributes
        Parameters:
        isbn: A 13-digit number starting in "978" or "979" that
        uniquely identifies the book
        title: The title of the book
        author: Name of the author
        year: The year the book was published
        format: The format of the book as "Hardcover",
                "Softcover", "Kindle", or "PDF"
        filename: Name of the file containing the text of the book
        """
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
        try:
            self.isbn = isbn
            self.title = title
            self.author = author
            self.year = year
            self.filename = filename
            self.format = format
            try:
                file = open(self.filename, 'r')
                file_data = file.readlines()
                file.close()
                sentences, words, syllables = analyze_file_data(file_data)
                index = flesch_index(sentences, words, syllables)
                self.flesch_grade = flesch_grade(index)
            except ValueError:
                raise ValueError("Error occurred while calculating the " +
                                 "Flesch grade" + self.title)
        except FileNotFoundError:
            raise ValueError("Invalid filename provided to this Book")
        except PermissionError or OSError:
            raise ValueError("Invalid file provided to this Book")

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_format(self):
        return self.format

    def get_filename(self):
        return self.filename

    def get_readability_grade(self):
        return self.flesch_grade

    def get_index(self):
        """
        This method dynamically generates an index of all the words
        in the book in a strange way
        input: self.file_data
        output:
            index: a dictionary which corresponds every word in this
                   book and its frequency
        """
        def add_word(word, index, line):
            """
            This helper function helps to add a word to target dictionary
            Parameter:
                word: the word to put into the dictionaty
                index: the target dictionary where we put the word in
                line: the string where we get word from
            Return: None
            """
            if word == "":
                return
            word = word.lower()
            if word not in index:
                index[word] = 0
            index[word] += 1

        space_and_punct = {" ", "!", ":", ";", ".", "?", ","}
        index = dict()
        # a cache to save the incomplete word
        save = ""
        # marks whether a word ends in a line
        to_be_continue = False
        file = open(self.filename, 'r')
        file_data = file.readlines()
        file.close()
        try:
            for line in file_data:
                line = line.strip()
                # first pointer
                start = 0
                # last pointer
                end = 0
                # count for consequent punctuations
                tmp = 0
                for letter in line:
                    if end == len(line) - 1 and letter == "-":
                        to_be_continue = True
                        save += line[start:end]
                    elif letter in space_and_punct:
                        tmp += 1
                        continue
                    elif tmp != 0:
                        if not to_be_continue:
                            add_word(line[start:end], index, line)
                        else:
                            word = save + line[start:end]
                            add_word(word, index, line)
                            to_be_continue = False
                            save = ""
# Overcome the punctuations and reset punctuation-markers
                        end += tmp
                        start = end
                        tmp = 0
                    end += 1
                if to_be_continue:
                    continue
# We should add last word of a line if it doesn't end with a punct of '-'
                else:
                    add_word(line[start:end], index, line)
            return index
        except ValueError:
            raise ValueError("Error occurred while generating the index for"
                             + self.title)

    def __str__(self):
        return self.title + " by " + self.author + ", " + str(self.year) +\
               "\n" + "ISBN: " + self.isbn + ", " + self.format +\
               ", " + str(self.flesch_grade) + ", " + self.filename
