import os
import uuid
import random
import string


def get_file_path(instance, filename):
    """
    Generator of image upload path.

    Example:
    instance = Article.
    filename = image.png.
    """

    ext = filename.split('.')[-1]  # .png
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join(instance.__class__.__name__.lower(), filename)


def gen_page_list(page_number, page_count):
    # Generate list with pagination.

    page_number = int(page_number)
    my_page = []
    if page_count > 5:
        if page_number <= 4:
            for key in range(1, 5):
                my_page.append(key)
            my_page.append('...')
            my_page.append(page_count)
        elif page_number >= (page_count - 4):
            my_page.append(1)
            my_page.append('...')
            for key in range((page_count - 3), page_count + 1):
                my_page.append(key)
        else:
            my_page.append(1)
            my_page.append('...')
            for key in range((page_number - 1), (page_number + 2)):
                my_page.append(key)
            my_page.append('...')
            my_page.append(page_count)
    else:
        for key in range(0, page_count):
            my_page.append(key + 1)
    return my_page


def generate_random_data(length=None, type=None):
    """
    Random data generator.
    It's can be string, integer, float, datetime, time.
    Function take length - it's a number of symbol of result data and object type.
    It's mean result will be that object type.
    """

    if type == 'string':
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    elif type == 'integer':
        return int(''.join(random.choice(string.digits) for i in range(length)))

    elif type == 'float':
        return float(''.join(random.choice(string.digits) for i in range(length)))

    # Datetime format '2017-02-18' or 'YYYY-MM-DD'
    elif type == 'datetime':
        year = random.randint(1990, 2018)

        month = random.randint(1, 12)
        if month < 10:
            month = '0{0}'.format(month)

        day = random.randint(1, 28)
        if day < 10:
            day = '0{0}'.format(day)
        return '{0}-{1}-{2}'.format(year, month, day)

    # Time format '01:30' or 'HH:MM'
    elif type == 'time':
        hour = random.randint(0, 23)
        if hour < 10:
            hour = '0{0}'.format(hour)

        minute = random.randint(0, 60)
        if minute < 10:
            minute = '0{0}'.format(minute)

        return '{0}:{1}'.format(hour, minute)

    # If type not correct we return None
    else:
        return None
