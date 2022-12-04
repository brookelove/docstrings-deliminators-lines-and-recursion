import string


def remove_punc(lst):
    # print(str)
    no_punc_lst = []
    # print(lst)
    for w in lst:
        for l in w:
            if l in string.punctuation:
                w = w.replace(l, "")
        no_punc_lst.append(w)

        #         j.replace(i, '')
        # no_punc_lst.append(i)
    return no_punc_lst
# no_punc = ''
# for i in str:
#     if i in string.punctuation:
#         no_punc = no_punc.replace(i, "")
# return no_punc


def list_to_twice(lst):
    # print("list_to_twice function") # double check that we are in the function
    # print(lst)
    count_dict = {}
    twice_list = []
    for w in lst:
        if w in count_dict:
            count_dict[w] += 1
        else:
            count_dict[w] = 1
    # print(count_dict)
    for i in count_dict:
        # print(count_dict.get(i))
        if count_dict.get(i) == 2:
            # print("twice")
            # print(i)
            twice_list.append(i)
    return twice_list


def results(lst):
    str_lst = ', '.join(lst)
    if len(lst) > 1:
        print(f"The words that appear twice in your file is: {str_lst}")
    else:
        print(f"The word that appears twice in your file are: {str_lst}")


def read_file():
    file_input = input(
        "Please input a file that you would like to have analyzed: ")
    with open(f"{file_input}.txt", "r") as f:
        # print(f)
        # print(remove_punc(f))
        # print(type(f))
        # print(str(f).maketrans('', '', string.punctuation))
        # str_file = str(f)
        for w in f:
            w = w.upper()
            line_lst = (w.split())
        remove_punc_lst = remove_punc(line_lst)
        two_result = list_to_twice(remove_punc_lst)
        # print(f"The file reads as: {str_file}")
        results(two_result)


read_file()
