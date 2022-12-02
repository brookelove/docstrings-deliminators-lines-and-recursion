import string


VOWELS = ['A', 'E', 'I', 'O', 'U']
v_lst = []
c_lst = []
sentence_lst = []

# counts the letters out of the list and put it in vowel dictionary


def vowel_counter(line):
    # counts the letter of consonants and put in in the dictionary
    print(line)
    # pass


def consonant_counter(line):
    print(line)
    # relies on the counter wil be raising errors
    #  pass


def vc_counter(filename):
    for lines in filename:
        vowel_counter(lines)
        consonant_counter(lines)

# def get_file_input():
#     done = False
#     while not done:
#         print()


def read_file():
    # main function where the try and catch that will read the file and try to run vc_counter function
    # complete = False
    while True:
        file_input = input("Enter the name of a text file: ")
        try:
            # with function automatically closes file
            with open(f"{file_input}.txt", "r") as f:
                vc_counter(f)
            print(f"Total # of vowels in the text file: {v_lst}")
            print(f"Total # of consonants in text file: {c_lst}")
            break
            # complete = True
        except FileNotFoundError as e:
            print("Could not find file, please try again: ", e)
            continue
            # raise FileNotFoundError


read_file()
