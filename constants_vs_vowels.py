import string


VOWELS = ['A', 'E', 'I', 'O', 'U']
v_lst = []
c_lst = []
sentence_lst = []

# counts the letters out of the list and put it in vowel dictionary


def vowel_counter(line):
    '''loops through letters in a read line to append vowels to v_lst in the current line'''
    # counts the letter of consonants and put in in the dictionary
    # print(line) # prints uppercase line
    for letter in line:
        # print(letter)
        if letter in VOWELS:
            v_lst.append(letter)
    # pass


def consonant_counter(line):
    '''loops through letters in a read line to append consonants to c_lst in the current line'''
    # print(line) #prints uppercase line
    for letter in line:
        if letter not in VOWELS and letter not in string.punctuation and letter not in string.digits:
            c_lst.append(letter)
        # print(letter)  # prints uppercase letter
        # relies on the counter wil be raising errors
        #  pass


def vc_counter(filename):
    '''loops through lines in letter, creates them to be uppercase and passes lines into two functions'''
    for lines in filename:
        upper_lines = lines.upper()  # converts line to uppercase
        vowel_counter(upper_lines)
        consonant_counter(upper_lines)

# def get_file_input():
#     done = False
#     while not done:
#         print()


def read_file():
    # main function where the try and catch that will read the file and try to run vc_counter function
    # complete = False
    '''tries to ask user input to get the correct name of a text file on a loop'''
    while True:
        file_input = input("Enter the name of a text file: ")
        try:
            # with function automatically closes file
            with open(f"{file_input}.txt", "r") as f:
                vc_counter(f)
            break
            # complete = True
        except FileNotFoundError as e:
            print("Could not find file, please try again: ", e)
            continue
            # raise FileNotFoundError


read_file()
vowel_num = "{:,.}".format(len(v_lst))
consonant_num = "{:,.}".format(len(c_lst))
print(c_lst)
print(v_lst)
print(f"Total # of vowels in the text file: {vowel_num}")
print(f"Total # of consonants in text file: {consonant_num}")
