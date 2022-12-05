import string


class NotAnIntegerError(Exception):
    pass


class NotAPositiveError(Exception):
    pass


def factorial(num):
    # print("factorial") # check to see if we are in the correct area
    # int_num = int(num)
    if num == 1:
        return num
    else:
        # print(int_num * factorial(int_num - 1))
        # print(2*3)
        # fact_result = (int_num * factorial(int_num - 1))
        # print(fact_result)
        return num * factorial(num - 1)


def factorial2(num):
    result = 1
    for i in range(1, num+1):
        # result *= i
        result = result * i
    return result


# def get_user_input():
#     user_num = input(
#         "Please input a number that you would like to find the factorial of: ")
#     if int(user_num):
#         raise NotAPositiveError
#     elif :
#         raise NotAnIntegerError
#     factorial(int(user_num))
#     factorial2(int(user_num))
def fact_results(f1, f2):
    print(f"The results of the factorial using a recursive function are: {f1}")
    print(
        f"The results of the factorial using a non-recursive function are: {f2}")


def run_factoirals():
    done = False
    while not done:
        try:
            user_num = int(
                input("Please input a number that you would like to find the factorial of: "))
            if user_num < 0:
                raise NotAPositiveError
            done = True
            f1 = factorial(int(user_num))
            f2 = factorial2(int(user_num))
            fact_results(f1, f2)
        except ValueError:
            print("The value you printd is not an integer please try again")
        except NotAPositiveError:
            print(
                "The value that you inputed is negative, please enter apositive integer")


run_factoirals()
