import os
import random

def read_file_to_list(filename):
    """Doesn't currently tidy the data, strip newlines
    or anything like that"""
    source_text_file = open(filename, "r")
    source_text = source_text_file.read()
    word_list = source_text.split()
    source_text_file.close()
    return word_list

def make_dict(source_list):
    markov_dictionary = {}
    list_index = 0
    list_length = len(source_list)

    while list_index < (list_length - 2):
        word_one = source_list[list_index]
        word_two = source_list[list_index + 1]
        word_three = source_list[list_index + 2]
        key_string = word_one + " " + word_two

        if not key_string in markov_dictionary:
            markov_dictionary[key_string] = [word_three]
        else:
            value = markov_dictionary[key_string]
            value.append(word_three)
            markov_dictionary[key_string] = value
        list_index = list_index + 1

    return markov_dictionary

def make_text(dictionary, iterations):
    key_list = []
    phrase_list = []
    output_string = ""
    starting_point = "null"
    iterations_initial_value = iterations
    for key in dictionary:
        key_list.append(key)
    starting_point = random.choice(key_list)
    while iterations > 0:

        new_word = random.choice(dictionary.get(starting_point))
        new_phrase = starting_point + " " + new_word + " "

        output_string += new_phrase

        #SET NEW STARTING POINT HERE
        phrase_list = new_phrase.split()
        if len(phrase_list) == 2:
            starting_point = phrase_list[1] + " " + phrase_list[2]
        else:
            starting_point = random.choice(key_list)
        iterations -= 1

    #Ending it
    ##if the last char isn't a comma, semicolon or period, iterate again
    ##OR slice to last punctuation?
    return output_string

def incantation():
    output = read_file_to_list("incantation_source.txt")
    dict = make_dict(output)
    output = make_text(dict, 50)
    return output
