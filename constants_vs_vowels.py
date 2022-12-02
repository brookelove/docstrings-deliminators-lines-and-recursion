import string


VOWELS = ['A', 'E', 'I', 'O', 'U']
vowel_dict = {}
consonant_dict = {}
sentence_lst = []

# counts the letters out of the list and put it in vowel dictionary


def vowel_counter():
    # counts the letter of consonants and put in in the dictionary
    pass


def consonant_counter():
    # relies on the counter wil be raising errors
    pass


def vc_counter(filename):
    return filename


# def get_file_input():
#     done = False
#     while not done:
#         print()


def read_file():
    # main function where the try and catch that will read the file and try to run vc_counter function
    # complete = False
    while True:
        file_input = input("Enter a text file: ")
        try:
            with open(file_input, "r") as f:  # with function automatically closes file
                for lines in vc_counter(f):
                    print(lines)
                break
                # complete = True
        except FileNotFoundError as e:
            print("Could not find file: ", e)
            continue
            # raise FileNotFoundError


read_file()
