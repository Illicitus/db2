import string

# I can write, but don't use next one string function, because it's not always simple to read and debug:
# len([my_list for item in range(number1, number2 + 1) if item % number3 == 0])


def handle_numbers(number1, number2, number3):
    """
    Takes 3 params and return count of numbers between number1 and number2,
    with divisible on number3 without remainder.
    """
    my_list = []

    for item in range(number1, number2 + 1):
        if item % number3 == 0:
            my_list.append(item)

    return len(my_list)


def handle_string(value):
    """
    Takes sentence and return the number of letters and digits in it.
    The letter register does not matter.
    """

    letters = 0
    digits = 0

    for item in value:
        if item in string.ascii_letters:
            letters += 1
        elif item in string.digits:
            digits += 1

    return 'Letters - {0}'.format(letters) + '\n' + 'Digits - {0}'.format(digits)


def handle_list_of_tuples(my_list):
    """
    Takes a list and sort it based on the next rules:
    name / age / height / weight
    """

    sorted_list = sorted(my_list, key=lambda x: (x[3], x[2], x[1]), reverse=True)  # sort on secondary keys, descending
    sorted_list = sorted(sorted_list, key=lambda x: x[0])   # sort on primary key

    return sorted_list
