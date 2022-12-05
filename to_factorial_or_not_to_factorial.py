import string


class NotAnIntegerError(Exception):
    pass


class NotAPositiveError(Exception):
    pass


def factorial(num):
    print("factorial")


def factorial2(num):
    print("factorial 2")


# def get_user_input():
#     user_num = input(
#         "Please input a number that you would like to find the factorial of: ")
#     if int(user_num):
#         raise NotAPositiveError
#     elif :
#         raise NotAnIntegerError
#     factorial(int(user_num))
#     factorial2(int(user_num))


def run_factoirals():
    done = False
    while not done:
        try:
            user_num = int(
                input("Please input a number that you would like to find the factorial of: "))
            if user_num < 0:
                raise NotAPositiveError
            factorial(int(user_num))
            factorial2(int(user_num))
        except ValueError:
            print("The value you printd is not an integer please try again")
        except NotAPositiveError:
            print(
                "The value that you inputed is negative, please enter apositive integer")


run_factoirals()
