import string
import operator
sentence = "Wwwas iiit a rat I saw?"


def letter_count(str):
    # count = 1
    count_dict = {}
    '''Counts the frequency of letters in a sentence and returns it as a dictonary'''
    uppercase = str.upper()
    # print(uppercase) # prints string in uppercase
    for letter in uppercase:
        # print(letter)  # prints each letter
        # print(count)
        if letter in string.ascii_uppercase:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
        # if letter in count_dict:
        #     print(letter)
        #     count += 1
        #     print(count)
        #     count = 0
        # elif letter in string.ascii_uppercase:
        #     print(letter)
        #     count += 1
        #     print(count)
        # if letter in count_dict:
        #     count = count_dict.get(letter)
        #     count += 1
        # elif letter in string.ascii_letters:
        #     count += 1
        #     count_dict[letter] = count
        #     count = 0
        sorted_dict = dict(sorted(count_dict.items()))

    return sorted_dict


def most_common_letter(str):
    common_lst = []
    lett_lst = []
    sorted_dict = letter_count(str)
    # print(sorted_dict)  # letters sort
    sort_by_value = sorted(sorted_dict.items(), key=operator.itemgetter(1))
    #value_dict = dict(sort_by_values)
    # print(value_dict)  # returns the information as a dictionary
    # print(sort_by_values[-1])  # getrs last tuple in list
    sort = sort_by_value.pop(-1)
    # print(sort)
    common_lst.append(sort)
    # print(sort_by_value[-1][1])  # gets last element in the list of tuples

    for i in sort_by_value:
        # print(i[1])
        if i[1] == sort_by_value[-1][1]:
            # print(i) # prints tuple
            common_lst.append(i)
    for i in range(len(common_lst)):
        # print(common_lst[i][0]) # letters
        lett_lst.append(common_lst[i][0])
    lett_lst.append(sort_by_value[-1][1])
    return lett_lst


def string_count_histogram():
    pass


def results():
    pass


def get_sentence():
    letter_count(sentence)
    most_common_letter(sentence)


get_sentence()
