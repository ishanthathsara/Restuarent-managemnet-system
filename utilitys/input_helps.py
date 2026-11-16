class RestuarentError(Exception):
    pass

def get_non_empty_str(prompt):

    while True:
        try:

            value = str(input(prompt)).strip().lower()

            if value:
                return value

            print("input can't be empty")
        except RestuarentError:
            raise "Enter valid answer please"

def get_int_input(prompt,minimum : int | None = None,maximum :int | None = None):

    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"value must be at least {minimum}")
                continue

            if maximum is not None and value > maximum:
                print(f"value must be less than {maximum}")
                continue

            return value

        except RestuarentError:
            raise "Enter integer please "

def get_float_input(prompt,minimum : int | None = None,maximum :int | None = None):

    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"value must be at least {minimum}")
                continue

            if maximum is not None and value > maximum:
                print(f"value must be less than {maximum}")
                continue

            return value

        except RestuarentError:
            raise "Enter integer please "

def choose_two_options(option_one,option_two):
    while True:
        user_option = input("Enter your option here : ")
        if user_option == option_one:
            return option_one
        elif user_option == option_two:
            return option_two
        else:
            print("invalid user option")



