import math
import os


def get_environment_int(value_name, default_value):
    try:
        return int(os.getenv(value_name, default_value))
    except (ValueError, TypeError):
        return default_value


def get_environment_list(value_name, default_value):
    try:
        return os.getenv(value_name, default_value).lower()
    except (ValueError, TypeError):
        return default_value


def get_scale_probability_as_fraction(scale, a, b, v=1):
    # (b/a) is the scale 1 vector average for consecutive same polarity ticks
    # where a < b

    # (a/b) gives the probability of a polarity flip
    # (1 - a/b) gives the probability of a polarity continuation

    nominator = math.pow(b + (1 * a * scale) - (2 * a), v - 1) * a * scale
    denominator = math.pow(b + (2 * a * scale) - (2 * a), v)

    return nominator, denominator


def get_model_average_for_all_scales(scale_max, a, b):
    vector_array = []

    for s in range(1, scale_max + 1):
        nominator, denominator = get_scale_probability_as_fraction(s, a, b)
        if denominator > 0:
            vector_array.append(nominator / denominator)
        else:
            vector_array.append(0.00)

    return vector_array


def show_array(vector_array, brackets=True):
    if not len(vector_array):
        return '{}'

    if type(vector_array[0]) == float:
        format_string = '.04f'
    elif type(vector_array[0]) == int:
        format_string = '2d'
    else:
        format_string = '>6s'

    vector_string = ''

    for value in vector_array:
        vector_string += f' {value:{format_string}},'

    vector_string = vector_string[:-1]

    if brackets:
        vector_string = f'{{{vector_string} }}'

    return vector_string


def sign(n):
    return (n > 0) - (n < 0)


def ave_abs(buffer):
    if len(buffer) > 0:
        return sum(map(abs, buffer)) / len(buffer)

    return 0.00


def tri_area(a, b):
    try:
        # heron's formula
        ave = (a + b) / 2
        return 0.25 * math.sqrt((a + (b + ave)) * (ave - (a - b)) * (ave + (a - b)) * (a + (b - ave)))
    except (ValueError, TypeError):
        return 0.00


def lucas_sequence(n, sequence_list=None):

    if sequence_list is None:
        sequence_list = [1, 1]

    if n > 2:
        for f in range(n - 2):
            sequence_list.append(sequence_list[f] + sequence_list[f + 1])

    return sequence_list
