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
    """Now a deprecated function"""
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

def make_two_dict(source_list):
    markov_dictionary = {}
    list_index = 0
    list_len = len(source_list)

    while list_index < (list_len - 1):
        word_one = source_list[list_index]
        word_two = source_list[list_index + 1]
        if not word_one in markov_dictionary:
            markov_dictionary[word_one] = [word_two]
        else:
            value = markov_dictionary[word_one]
            value.append(word_two)
            markov_dictionary[word_one] = value
        list_index = list_index + 1
    return markov_dictionary

def make_two_text(dictionary, iterations, name):
    key_list = []
    for key in dictionary:
        key_list.append(key)
        print(key)

    current_word = random.choice(key_list)
    output_string = current_word

    while iterations > 0:
        next_word_options = dictionary.get(current_word)
        if next_word_options:
            next_word = random.choice(next_word_options)
        else:
            next_word = "DEMON_NAME"
        output_string += " " + next_word
        current_word = next_word
        iterations -= 1
    #Ending it
    next_word_options = dictionary.get(current_word)

    while (next_word == "and") or (next_word == "the") or (next_word == "or"):
        if next_word_options:
            next_word = random.choice(next_word_options)
        else:
                next_word = "DEMON_NAME"
        output_string += " " + next_word
        current_word = next_word

    output_string = output_string.rstrip()
    if output_string[-1] == ";" or output_string[-1] == ";":
        output_string += "!"
    elif output_string[-1] != ".":
        output_string += "!"
    return output_string


def make_text(dictionary, iterations, name):
    """Now a broken and deprecated function"""
    key_list = []
    phrase_list = []
    current_string = ""
    starting_point = "null"
    iterations_initial_value = iterations
    for key in dictionary:
        key_list.append(key)

    starting_point = random.choice(key_list)
    #print(starting_point)

    next_word_options = dictionary.get(starting_point)

    next_word = random.choice(next_word_options)

    current_string = starting_point + " " + next_word 
    output_string = current_string
    #print(current_string)

    while iterations > 0:
        current_phrase_split = current_string.split()

        second_starting_point = current_phrase_split[1] + " " + current_phrase_split[2]
        #print(second_starting_point)

        next_word_options = dictionary.get(second_starting_point)
        #print(next_word_options)

        if next_word_options:
            next_word = random.choice(next_word_options)
        else:
            next_word = "DEMON_NAME"

        current_string = second_starting_point + " " + next_word + " "
        output_string += " " + next_word

        iterations -= 1
    #Ending it
    output_string = output_string.rstrip()
    if output_string[-1] == ";" or output_string[-1] == ";":
        output_string += "!"
    elif output_string[-1] != ".":
        output_string += "!"
    print(output_string)
    print("\n")
    return output_string

def incantation(length, name):
    output = read_file_to_list("incantation_source.txt")
    our_dict = make_two_dict(output)
    output = make_two_text(our_dict, length, name)
    return output
