import string
import operator
import sys
sentence = "Wwwas iiit a rat I saw?"


def letter_count(str):
    # count = 1
    count_dict = {}
    '''Counts the frequency of letters in a sentence and returns it as a dictonary'''
    uppercase = str.upper()
    # print(uppercase) # prints string in uppercase
    if len(uppercase) < 15:
        print("Please enter a senter that is longer than 15 characters")
    else:
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
    '''sorts dictionary by values and appends the most common value to a list'''
    common_lst = []
    lett_lst = []
    sorted_dict = letter_count(str)
    # print(sorted_dict)  # letters sort
    sort_by_value = sorted(sorted_dict.items(), key=operator.itemgetter(1))
    # value_dict = dict(sort_by_values)
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


def string_count_histogram(str):
    '''prints the current letter from the dictionary the amount of times that it shows in the given sentence'''
    sorted_dict = letter_count(str)
    letter_lst = []
    letter_tup = ()
    # print(sorted_dict) # prints sorted lst
    # for i in sorted_dict:
    #     # print(sorted_dict.get(i))
    #     num_lst.append(sorted_dict.get(i))
    # print(num_lst)
    # for i in num_lst:
    #     # print(i)
    #     for j in range(i):
    #         print(sorted_dic)
    for i in sorted_dict:
        # print(i)
        num = sorted_dict.get(i)
        # num = sorted_dict[i].values()
        # print(num)
        for j in range(num):
            # print(i)
            letter_lst.append(i)
        #     letter_tup = letter_tup + (i,)
        # letter_lst.append(letter_tup)
        # letter_tup = ()
    # print(letter_lst)  # prints list of tuples
    return letter_lst
    # print(list(sorted_dict)[i])  # returns the values
    # for j in range(sorted_dict.get(i)):
    #     print(list(sorted_dict))


def results(f1, f2, f3):
    '''takes in functions and returns as a print statemnt statments'''
    # join_letters = []
    str_letter_count = str(f1).replace("{", "").replace("}", "")
    letter_no_count = str(f2[0:-1]).replace("[", "").replace("]", "")
    # print(f3)
    hist_lst = f3
    new_hist_lst = []
    # print(f3.index("A"))
    for i, j in zip(hist_lst, hist_lst[1:]):
        # print(i, j)
        if i != j:
            # print("here")
            # print(hist_lst.index(i))
            new_hist_lst.append(i + "\n")
        else:
            new_hist_lst.append(i)
            # print(hist_lst.index(i))
            # hist_lst.insert(hist_lst.index(i), "\n")
    # print(hist_lst)
    # print(new_hist_lst)
    str_new_hist = ''.join(new_hist_lst)
    # for i in f3:
    #     # print(i)
    #     # print(f3.index(i) + 1)
    #     if i != f3[0]:
    #         print(f3.index(i)-1)
    #         print("not equal")
    #         # print(f3)
    # for i in f3:
    #     print(i)

    # for i in range(0, len(f3)):
    #     for j in range(i+1, len(f3)):
    #         # print(i) # returns index
    #         # print(j) # returns index
    #         print(f3[i])
    #         if f3[i] != f3[j]:
    #             print("here")
    # for i in range(len(f3)):
    #     # print(i)
    #     add_new_line = f3[i] + tuple("\n")
    #     joined_str = ''.join(add_new_line)
    #     join_letters.append(joined_str)
    # joined_str = str(join_letters).replace(
    #     "[", "").replace("]", "").replace("'", "").replace(",", "")
    # print(add_new_line)
    # print(f3.index(l))
    # print(''.join(f3))
    # print(''.join(letter_no_count))
    # print(letter_no_count)
    print(f"1. Letter counts: {str_letter_count}")
    if len(f2) > 2:
        print(
            f"2. Most frequent letters: {letter_no_count} each appear {f2[-1]} times.")
    else:
        print(f"2. Most frequent letters: {f2[1]} each appear {f2[-1]} times.")
    print(f"Histogram:\n{str_new_hist}")


# def get_sentence():
if __name__ == '__main__':
    l = letter_count(sentence)
    m = most_common_letter(sentence)
    s = string_count_histogram(sentence)
    results(l, m, s)


# get_sentence()
