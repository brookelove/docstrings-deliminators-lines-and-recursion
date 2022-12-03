import string
sentence = "Was it a rat I saw?"
count_dict = {}


def letter_count(str):
    count = 0
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

    return print(sorted_dict)


def most_common_letter():
    pass


def string_count_histogram():
    pass


def results():
    pass


def get_sentence():
    letter_count(sentence)


get_sentence()
