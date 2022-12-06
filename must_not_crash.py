import string


def mathmatics(str):
    # print(str)
    num_lst = list(str)
    # print(num_lst)
    for i in num_lst:
        if i == ',':
            num_lst.remove(i)
    # print(num_lst) # shows lists without extra num
    # print(num_lst)
    # print(len(num_lst))
    for i in num_lst:
        if i in string.ascii_letters or i in string.punctuation:
            raise ValueError
    if len(num_lst) > 4:
        raise IndexError
    elif num_lst[-1] == 0:
        raise ZeroDivisionError

    # print(num_lst)
    mult_num = int(num_lst[0]) * int(num_lst[1])
    # print(mult_num) # prints numbers
    add_num = mult_num + int(num_lst[2])
    # print(add_num)
    div_num = add_num/int(num_lst[3])
    return print(f"(({num_lst[0]} + {num_lst[1]}) + {num_lst[2]}) / {num_lst[3]} = {div_num}")


def run_math():
    done = False
    while not done:
        try:
            user_input = input(
                "Please enter 4 numbers that are seperated by commas (,): ")

            mathmatics(user_input)
            done = True
        except ValueError:
            print("The number that you entered is not a valid number")
        except ZeroDivisionError:
            print(
                "The last number that you inputted was 0 and it cannot be divided by 0, please try again.")
        except IndexError:
            print(
                "Your numbers exceed the index, please try entering 4 integers seperated by commas.")


run_math()
